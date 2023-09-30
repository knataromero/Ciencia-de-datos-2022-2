#!/usr/bin/env python
# coding: utf-8

# ![logocutre.JPG](attachment:logocutre.JPG)

# # LA EXTRACCIÓN EN EL  PROCESO ETL

# ## acerca de mi ...
# 
# Soy *Karen Natalia Romero* , actualmente tengo 22 años y me encuentro cursando mi último semestre de Economía en la Universidad Nacional de Colombia. Me caracterizo por ser una persona curiosa con amplios intereses en variados campos, y estoy buscando aprender todas las herramientas que tengo a mi alcance para poder solucionar problemas del **mundo real** y mejorar la calidad de vida de las personas a mi alrededor. Mediante la pasantia que actualmente estoy realizando en el banco de la república, he podido fortalecer habilidades de manejo  y analisis de datos, programación básica, extracción de datos de diversas fuentes y elaboracion de informes. 
# 
# Dejo una foto de mi, en el chiripazo de haber entrado justo el año en que el banco cumplia su primer centenario.

# ![WhatsApp%20Image%202023-09-29%20at%2010.09.31%20PM%20%281%29.jpeg](attachment:WhatsApp%20Image%202023-09-29%20at%2010.09.31%20PM%20%281%29.jpeg)

# Ahora si, pasamos al concepto ETL
# 
# ## El proceso ETL
# 
# Si bien es cierto que lo primero que viene en mente al mencionar "datos" en cualquier proyecto  usualmente son los modelos o tecnicas que se utilizaran, el proceso ETL es **fundamental** ya que es el pilar de todo. 
# 
# No se puede trabajar con datos si  estos no son accesibles en un cierto formato que permita el trabajo  con ellos. 
# 
# 
# ### EXTRACCIÓN
# 
# Por ello, es de suma importancia realizar el proceso ETL correctamente. En primer lugar, se tiene la *extracción* de los datos, que se refiere a tomar la información de las fuentes donde se encuentra disponible. Suena fácil, en principio, pero esto puede llegar a ser muy engañoso. Como ejemplo, tomaré una base de datos que construi en el banco para una de las investigaciones en curso. 
# 
# EL objetivo principal era recolectar datos fiscales de 6 países diferentes en la región de latinoamerica incluyendo Argentina, Brasil, Chile, Colombia, Mexico y Perú. En principio, la informacion era "fácil" de extraer puesto que esa información se encuentra en las entidades públicas de cada país. Sin embargo, no  fue así: en muchos casos no estaba disponible la información historica, por lo que debi escribir y esperar su respuesta; en algunos casos no estaba en formato excel ni CSV sino en **pdf**, por lo que se complicaba la compilación de la información. 
# 
# En otros casos, las cifras estaban fragmentadas y fue necesario cruzarla con varias fuentes para llegar al resultado final. Por ejemplo, el balance primario se define como: 
#  
# 

# $$Balance \; primario = Ingresos\;- Gastos \;sin \;pago \; deuda$$

# Pero, esto debe hacerse con cada entidad pública del gobierno central, por lo que la ecuación luce como: 

# $$Balance \;primario = \sum_{i}^{n} (Ingresos_i\; - \;Gastos_i) $$

# Donde *n* corresponde  al total de entidades publicas. Es un proceso sencillo pero muy largo y meticuloso, puesto que se debe explorar enlace por enlace  y pestaña por pestaña en páginas que aunque son de acceso público, no necesariamente son amigables o prácticas, como [esta](https://www.gob.pe/institucion/mef/tema/presupuesto), donde si bien se indica una categoria especifica, en verdad no se encuentra la informacion alli, y para encontrarla es necesario buscar y rebuscar dentro de las páginas.
# 
# Este proceso lo hice manualmente, pero cuando los datos se encuentran publicados de una forma mas estructurada pueden implementarse modelos de *web scrapping* para extraer la información de uan forma más automátizada. 
# 
# Ahora, luego de finalmente extraer la información y tenerla en formato Excel, corresponde el siguiente paso de *Transformar* los datos, teniendo en cuenta que se quiere una base de datos homogenea, en frecuencias mensuales, con variables en moneda nacional, dólar estadounidense, porcentaje del PIB, etc. Sin embargo, eso corresponde al segundo paso que se explicará en otra oportunidad. 
# 

# ### REFERENCIAS

# Ministerio de economía y finanzas. (2023). Presupuesto. Plataforma digital única del gobierno de Perú. República del Perú. Recuperado de: https://www.gob.pe/institucion/mef/tema/presupuesto 
# 
# Kumar, S.(2021). Data Science Regular Bootcamp: ETL Project. GitHub. https://github.com/imsanjoykb/Data-Science-Regular-Bootcamp/tree/master/ETL%20Project 
