import subprocess

def terraform_run(command):
    subprocess.run(command, shell=True, check=True)

directory = r"C:\Users\harsh\Desktop\Python-For-Devops\day-01\practice\terra_automate\Wanderlust-Mega-Project\terraform"
#command = f"terraform -chdir={directory} init"
command = f"terraform -chdir={directory} destroy -auto-approve"

terraform_run(command)
