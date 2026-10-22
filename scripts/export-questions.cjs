const path = require('node:path');
const fs = require('node:fs');
const vm = require('node:vm');
const ts = require('typescript');

const root = path.resolve(__dirname, '..');
const modules = new Map();

function load(relativePath) {
  const file = path.resolve(root, relativePath);
  if (modules.has(file)) return modules.get(file);
  const exports = {};
  modules.set(file, exports);
  const source = ts.transpileModule(fs.readFileSync(file, 'utf8'), {
    compilerOptions: { module: ts.ModuleKind.CommonJS },
  }).outputText;
  vm.runInNewContext(source, {
    exports,
    require: name => name.startsWith('.')
      ? load(path.resolve(path.dirname(file), name.endsWith('.ts') ? name : name + '.ts'))
      : require(name),
    console,
    URL,
  }, { filename: file });
  return exports;
}

const { BALOTARIOS_META, getQuestionsByCategory } = load('data/balotariosHelper.ts');

const result = {};

for (const [slug, meta] of Object.entries(BALOTARIOS_META)) {
  const questions = getQuestionsByCategory(slug);
  result[slug] = {
    meta: {
      code: meta.code,
      slug: meta.slug,
      className: meta.className,
      denomination: meta.denomination,
      shortDesc: meta.shortDesc,
      totalQuestions: questions.length,
    },
    questions: questions.map(q => ({
      id: q.id,
      subjectType: q.subjectType || 'Reglas de Tránsito',
      category: q.category || meta.code,
      topic: q.topic || q.subjectType || 'General',
      questionText: q.questionText,
      imageUrl: q.imageUrl || null,
      options: q.options || [],
      correctAnswerIndex: q.correctAnswerIndex ?? 0,
      legalBasis: q.legalBasis || '',
      explanation: q.explanation || '',
    }))
  };
}

const outputPath = path.join(__dirname, 'questions_dump.json');
fs.writeFileSync(outputPath, JSON.stringify(result, null, 2), 'utf8');
console.log(`Exported questions for ${Object.keys(result).length} categories to ${outputPath}`);
