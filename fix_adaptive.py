import re
from pathlib import Path

path = Path('src/inquisitio/runner/adaptive_racer.py')
text = path.read_text()
text = re.sub(r'mode=self\.accept_mode', '', text)
text = text.replace(', )', ')')
text = text.replace('mode=self.accept_mode', '')
path.write_text(text)
