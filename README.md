
Getting started.
----------------

Esta biblioteca suporta Python 2.7</br></br>
 Há duas maneiras de instalar a lib:

-  Instalação usando pip (Gerenciador de Pacotes do Python)\*:

::

    $ pip install requests
    $ pip install Barionix

-  Instalação pelo Source (necessário git):

::

    $ git clone https://github.com/JuniorMario/Barionix.git
    $ cd Barionix
    $ sudo mv /Barionix /usr/bin/python2.7/dist-packages/  
    /*Para o Python3 use o diretório do Python3, e para windows mova para o diretório do site-packages*/

Geralmente é recomendado a primeira opção.


<h1>Funções</h1>
<code><pre>
  Barionix.links(url) - retorna uma lista de links completos do site 
      Ex: (http://www.site.com)
  Barionix.dirs(url) - retorna uma lista de diretorios do site 
      Ex: (/JuniorMario/Barionix | /img/post/python-rules)
  Barinoix.href(url) - retorna uma lista de conteudo extraido das tags href do site 
      Ex: ("/JuniorMario/Barionix" | "https://github.com/JuniorMario/Barionix/edit/master/README.md")
    /*A tag sendo "<a href="/JuniorMario/Barionix"><span>Barionix</span></a>".*/.
  Barionix.getContent(url, 'p') - retorna uma lista de conteudo extraida de tag especifica.
  Barionix.imgs(url)  - retorna uma lista de links de imagens encontradas no site
      Ex: ("https://pythonwayblog.files.wordpress.com/2016/06/coffee-shop.jpg", https://pythonwayblog.files.wordpress.com/2016/06/camera041.jpg")
  Barionix.files(url) - retorna uma lista de arquivos encotrados no site
      Ex: ('http:www.site.com/files/arquivo.pdf')
  Barionix.getIn(url, '<atriburo>', Parametro) - retorna uma lista de conteudo extraido dentro de atributo.
  </pre></code>
  
<h1>Exemplos:</h1>
<h3>Obtendo Pdf do Bing</h3>
<blockquote>

<pre>
  import Barionix
  url = "https://www.bing.com/search?q=python+pdf"
  files = Barionix.files(url)
  for file in files:
        print file
</pre>
</blockquote>

<h3>Obtendo links</h3>
<blockquote>
<pre>
    import Barionix
    url = 'http://www.pythonforbeginners.com/' 
    links = Barionix.links(url)
    for i in links:
        print i

</pre>
</blockquote>

<h3>Obtendo conteudo da tag div</h3>
<blockquote>
<pre>
    import Barionix
    url = 'http://www.pythonforbeginners.com/' 
    get_tag = Barionix.getContent(url, 'div')
    for i in get_tag:
        print i
</pre>
</blockquote>
<h3>Obtendo fotos de um perfil do facebook</h3>
<blockquote>
<pre>
    import Barionix
    url = 'https://www.facebook.com/UniversoInteligente/?fref=ts' 
    get_pics = Barionix.imgs(url)
    for i in get_pics:
        print i
</pre>
</blockquote>
<h3>Obtendo conteudo do atributo class</h3>
<blockquote>
<pre>
    import Barionix
    url = 'http://www.pythonforbeginners.com/' #Definindo a url
    get_in_tag = Barionix.getIn(url, 'class', None)
    for i in get_in_tag:
        print i
</pre>
</blockquote>


Contato no Telegram: @Barionix.
