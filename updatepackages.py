import subprocess
import pkg_resources

# Tüm kurulu paketleri al
installed_packages = [pkg.key for pkg in pkg_resources.working_set]

# Paketleri güncelle
for package in installed_packages:
    subprocess.check_call(['pip', 'install', '--upgrade', package])
