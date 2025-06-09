import subprocess

def main():
    subprocess.run(["python", "run_analysis.py"], check=True)
    subprocess.run(["python", "report_generator.py"], check=True)
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Auto update analysis report"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("Pipeline executed: analysis, report generation, git push completed.")

if __name__ == "__main__":
    main()
