import subprocess
import sys

def install_libraries(libs):
    subprocess.call([sys.executable, "-m", "pip", "install", "--upgrade", *libs])

if __name__ == '__main__':
    libs = ['requests', 'python-telegram-bot']
    install_libraries(libs)

    files = [
        'chats.db',
        'filter.db',
        'global_stats.db',
        'rules.db',
        'save.db',
        'stats.db',
        'warn.db',
        'warn_limit.db',
        'welcome.db'
    ]

    for file in files:
        open(file, 'a').close()