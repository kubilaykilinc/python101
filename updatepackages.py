import subprocess
import pkg_resources

# Get all installed packages / Tüm kurulu paketleri al
installed_packages = [pkg.key for pkg in pkg_resources.working_set]

# Update packages / Paketleri güncelle
for package in installed_packages:
    subprocess.check_call(['pip', 'install', '--upgrade', '--user', package])
