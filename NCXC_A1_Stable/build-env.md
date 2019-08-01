conda create -n extranumpy python=3.7
activate extranumpy
conda install -c conda-forge numpy
pip install pyinstaller


pip install opencv-python
pip install wxPython
pip install PyPubSub

// NET
pip install scapy
pip install --pre scapy[basic]
pip install --pre scapy[complete]


-n : name
--pre : dev

pyinstaller D:\space-g8hp\NCIC_A2_Stable\NCIC.py --onefile -w -i NCIC.ico
pyinstaller NCIC.py --onefile -w -i NCIC.ico