import os

ad_head = '''<script async="async" data-cfasync="false" src="https://bauval.org/21/9aff43a332ea22fc4376626586e07289"></script>
<script data-cfasync="false" src="https://bauval.org/14/e0c00aa4d84ad9ced529198f1bb68d00"></script>
<script>
  atOptions = {
    'key' : '311ee48c51b2e1b5363f435eb21d053b',
    'format' : 'iframe',
    'height' : 250,
    'width' : 300,
    'params' : {}
  };
</script>
<script src="https://bauval.org/22/311ee48c51b2e1b5363f435eb21d053b"></script>'''

ad_body = '''<div style="display: flex; justify-content: center; margin: 20px 0;">
    <div id="container-9aff43a332ea22fc4376626586e07289"></div>
</div>'''

files = ['index.html', 'bosses.html', 'systems.html', 'quests.html', 'collectibles.html']

for f in files:
    if not os.path.exists(f):
        print(f'Skipping: {f}')
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    if '311ee48c51b2e1b5363f435eb21d053b' not in content:
        content = content.replace('</head>', ad_head + '\n</head>')
        print(f'Added head scripts: {f}')

    if 'container-9aff43a332ea22fc4376626586e07289' not in content:
        content = content.replace('<footer', ad_body + '\n\n<footer')
        print(f'Added container div: {f}')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Updated: {f}')
