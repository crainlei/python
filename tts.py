#!/usr/bin/python3

import sys
import os
import tempfile
from gtts import gTTS

mt = input("")
language = sys.argv[1]
voice = gTTS(text=mt, lang=language, slow=False)
new_file, path = tempfile.mkstemp()
voice.save(path)
os.system("mplayer " +  path + ">/dev/null 2>&1")

os.remove(path)
