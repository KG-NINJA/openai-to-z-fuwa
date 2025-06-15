import { execSync } from 'child_process'

try {
  execSync('python scripts/report_generator.py', { stdio: 'inherit' })
  console.log('Z log finalization completed.')
} catch (err) {
  console.error('Finalization failed', err)
  process.exit(1)
}
