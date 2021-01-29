import html
print(html.escape('This HTML fragment contains a <script>script</script> tag.')) # transforma os comandos > < para o valor em html-safe
print(html.unescape("I &hearts; Python's &lt;standard libraty&gt;.")) # transforma todos seus codigos em seus respectivos caracteres
