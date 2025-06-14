import { createAgent } from 'openai-agents'

const agent = await createAgent({
  name: 'ZFinalizerAgent',
  files: [
    './results/results.json',
    './templates/template.md',
    './scripts/report_generator.js',  // または .py を Nodeから叩く
  ],
  context: 'Create final Kaggle Z submission with cultural story, hypothesis, and NDVI analysis summary.',
})

await agent.runTask('Generate final PDF and Markdown summary for submission. Include cultural interpretation of O3 site.')
