sudo apt-get install p7zip-full
wget https://archive.org/download/stackexchange/stackoverflow.com-Tags.7z
7za x stackoverflow.com-Tags.7z
pip3 install -r req.txt
python3 xml_2_json.py Tags