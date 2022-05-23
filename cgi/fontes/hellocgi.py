#!/usr/bin/python3
import cgi

pedido = cgi.FieldStorage()

nome = pedido.getvalue('nome')
x = int(pedido.getvalue('x'))

print("Content-type: text/html\n\n")

for i in range(x):
        print("Hello %s<br />" % nome)

print("<br />em <b>Python</b><br />")
























                                        [ Read 14 lines ]
^G Help         ^O Write Out    ^W Where Is     ^K Cut          ^T Execute      ^C Location
^X Exit         ^R Read File    ^\ Replace      ^U Paste        ^J Justify      ^_ Go To Line
