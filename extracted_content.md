biología de las comunicaciones 

Artículo 

Una revista de Nature Portfolio 

https://doi.org/10.1038/s42003-025-08960-6 

Buscar actualizaciones 

Impulsando la predicción de la estructura terciaria de proteínas AlphaFold mediante ingeniería de MSA y muestreo y clasificación extensos de modelos en CASP16 

**==> picture [12 x 10] intentionally omitted <==**

Jian Liu1,2, Pawan Neupane1,2 y Jianlin Cheng 1,2 

AlphaFold2 y AlphaFold3 han revolucionado la predicción de la estructura de proteínas al permitir predicciones de alta precisión para la mayoría de proteínas de cadena única. Sin embargo, obtener predicciones de alta calidad para blancos difíciles con alineamientos de secuencias múltiples superficiales o con ruido y arquitecturas multic-domain complicadas sigue siendo desafiante. Presentamos MULTICOM4, un sistema integral de predicción de estructuras que utiliza generación diversa de MSA, muestreo a gran escala de modelos y una estrategia de evaluación de calidad de modelos en ensemble para mejorar la generación de modelos y el ranking de AlphaFold2 y AlphaFold3. En la 16ª Evaluación Crítica de Técnicas para la Predicción de Estructuras de Proteínas, nuestros predictores basados en MULTICOM4 estuvieron entre los mejores de 120 predictores en la predicción de estructura terciaria y superaron a un predictor estándar de AlphaFold3. Nuestro mejor predictor logró una TM-score media de 0.902 para 84 dominios CASP16, con predicciones de top-1 que alcanzaron alta precisión (TM-score>0.9) para 73.8% y pliegues correctos (TM-score>0.5) para 97.6% de los dominios. En predicciones de mejor-a-top-5, todos los dominios estuvieron correctamente plegados. Los resultados muestran que la ingeniería de MSA usando diferentes bases de datos de secuencias, herramientas de alineación y segmentación de dominios, junto con un muestreo extenso de modelos, es crucial para generar modelos estructurales precisos. Combinar métodos de QA complementarios con agrupamiento de modelos mejora aún más la fiabilidad del ranking. Estos avances proporcionan estrategias prácticas para modelar proteínas de cadena simple difíciles en biología estructural y descubrimiento de fármacos. 

Desde que el aprendizaje profundo se aplicó a la predicción de estructuras de proteínas en 2012-2011, ha progresado sustancialmente en los últimos 13 años. En particular, en 2020, AlphaFold revolucionó el campo al usar una arquitectura de transformador para predecir con precisión estructuras terciarias de la mayoría de proteínas de cadena única (monómeros) en CASP14. Luego se extendió a AlphaFold2-Multimer, que puede predecir estructuras cuaternarias de complejos de proteínas con mayor precisión que los métodos de acoplamiento existentes. En 2024, AlphaFold3, basado en una arquitectura de difusión, mejoró aún más la predicción de la estructura de proteínas e interacciones entre proteínas y otras moléculas. 

se generan pliegues. Las puntuaciones de calidad de modelos auto-prediсtos por AlphaFold (p. ej., plDDT) no pueden seleccionar de forma consistente buenos/mejores modelos para objetivos difíciles. Estos desafíos dificultan que los usuarios obtengan predicciones de alta calidad para ciertos objetivos difíciles usando AlphaFold. 

CASP14. Luego se extendió a AlphaFold2-Multimer, que puede predecir Para abordar estos desafíos, desarrollamos MULTICOM4, un sistema integrador estructuras cuaternarias de complejos de proteínas con mayor precisión que de predicción de estructuras de proteínas que mejora la predicción de los métodos de acoplamiento existentes. En 2024, AlphaFold3, basado en una estructuras terciarias basadas en AlphaFold2 y AlphaFold3 al mejorar su arquitectura de difusión, mejoró aún más la predicción de la estructura de entrada y salida. MULTICOM4 genera MSA diversos usando múltiples bases de proteínas e interacciones entre proteínas y otras moléculas. datos de secuencias de proteínas, diferentes herramientas de alineación y alineamientos basados en dominios como entrada para que AlphaFold genere A pesar de la alta precisión general de la predicción de estructuras terciarias modelos estructurales terciarios. Además, realiza un muestreo extenso de basada en AlphaFold, aún enfrenta dos desafíos significativos para algunos blancos modelos para explorar un gran espacio de conformaciones. Además, aplica proteicos difíciles cuyos MSA son superficiales o ruidosos y no contienen suficiente múltiples métodos de evaluación de calidad de modelos (QA) complementarios información de coevolución inter-residuo/inter-dominio. El primer desafío es (también llamados métodos de estimación de precisión del modelo (EMA)) y generar algunos modelos estructurales de alta calidad para ellos. El segundo clustering de modelos para clasificar y seleccionar las estructuras previstas desafío es seleccionar buenos modelos estructurales después de muchos modelos finales. con diferencias 

1 Departamento de Ingeniería Eléctrica e Informática, Universidad de Missouri, Columbia, MO, EE. UU. 2 NextGen Precision Health, Universidad de Missouri, Columbia, MO, EE. UU. correo electrónico: chengji@missouri.edu 

Communications Biology | (2025) 8:1587 

1 

Artículo 

https://doi.org/10.1038/s42003-025-08960-6 

En el experimento CASP16 de alcance comunitario de 2024, nuestro mejor predictor de rendimiento (nombre: MULTICOM) basado en MULTICOM4 ocupó el puesto 4 entre 120 predictores en la predicción de estructuras terciarias (monómeros). Si se cuenta a varios predictores del mismo grupo una sola vez, ocupó el 2.º lugar entre todos los grupos participantes. También superó de forma constante al servidor AlphaFold3 estándar. Los resultados demuestran que la integración de predicciones de estructuras AlphaFold2 y AlphaFold3, MSAs diversos, muestreo extenso de modelos y métodos de clasificación de modelos múltiples pueden mejorar aún más la predicción de estructuras terciarias, especialmente para objetivos difíciles. 

## nos centramos en analizar el rendimiento de nuestro predictor de estructura terciaria de mejor rendimiento, MULTICOM. 

La Figura 1B ilustra las puntuaciones Z de MULTICOM en los 75 dominios únicos. Una puntuación Z mayor que 0.0 significa que el modelo top-1 enviado por MULTICOM tiene una calidad mejor que la calidad media de los modelos top-1 de todos los predictores. Las puntuaciones Z promedio para MULTICOM son 0,287. Hay 4 dominios con puntuaciones Z mayores que 1,0, 56 dominios con puntuaciones Z superiores a 0 (calidad por encima del promedio) y 19 dominios con puntuaciones Z por debajo de 0 (calidad por debajo del promedio). 

Nuestros resultados también muestran que, con MSAs diversos y un muestreo extenso de modelos, AlphaFold2 y AlphaFold3 pueden generar modelos con pliegues correctos para todos los objetivos de predicción de estructuras terciarias de CASP16. Sin embargo, los métodos QA existentes aún no pueden seleccionar modelos correctos como predicción top-1 para todos los objetivos. Por lo tanto, la clasificación de modelos puede ser más difícil que la generación de modelos para objetivos difíciles. Es un gran desafío que debe abordarse en el futuro. 

## Resultados 

## Rendimiento global de los predictores MULTICOM en CASP16 

Durante CASP16, 120 predictores participaron en el desafío de predicción de estructuras terciarias de proteínas. Se les exigió predecir la estructura dada la secuencia de un objetivo proteico y enviar hasta cinco estructuras predichas por objetivo de regreso a CASP, pero la evaluación final se basa en el/los dominio(s) del objetivo. En total, se publicaron 59 objetivos proteicos con 85 dominios para la predicción. En esta evaluación, se excluyó T1249v2 (T1249v2-D1) porque su estructura nativa no está disponible para nosotros, resultando en 58 objetivos proteicos con 84 dominios. Cabe señalar que los 84 dominios se consideran unidades de evaluación que deben evaluarse como un todo de acuerdo con la definición oficial de CASP16, lo que puede no corresponder exactamente con los dominios estructurales independientes. A veces, dos o más dominios estructurales de un objetivo se tratan como una sola unidad de evaluación porque la orientación entre ellos puede preverse bien por algunos predictores de CASP16. La evaluación puede realizarse ya sea en predicciones top-1 o en predicciones mejor de cinco para un predictor. En este trabajo, informamos principalmente los resultados de predicciones top-1. Cabe destacar que este estudio se centra exclusivamente en la predicción de estructuras terciarias para objetivos monoméricos en CASP16. La evaluación de la precisión a nivel de interfaz de la predicción de estructuras de proteínas CASP16 se puede encontrar en otro estudio14. 

Para cuantificar el rendimiento relativo de los predictores CASP16, se utilizaron puntuaciones Z para evaluar la predicción top-1 de cada predictor para cada dominio. Siguiendo el protocolo oficial de evaluación de CASP16, la puntuación GDT-TS original de cada modelo se convirtió en puntuación Z basada en la media y la desviación típica de las puntuaciones GDT-TS de todos los modelos top-1 de todos los predictores. Luego, se excluyeron los modelos con puntuaciones Z inferiores a -2 para eliminar valores atípicos. La puntuación Z de cada modelo restante se recalculó con base en la media y la desviación típica de las puntuaciones GDT-TS de los modelos restantes. El rendimiento de cada predictor se determinó por la suma de las puntuaciones Z en todos los dominios. Siguiendo el protocolo oficial de CASP16, solo las puntuaciones Z mayores que 0 se acumularon para cada predictor. Además, para evitar contribuciones redundantes de conformaciones alternativas del mismo dominio, promediamos las puntuaciones Z para 18 pares de dominios alternativos (p. ej., T1228v1 y T1228v2, T1239v1 y T1239v2, T1294v1 y T1294v2) para incluirlos en la suma. La suma de la puntuación Z de 75 dominios únicos de los 84 dominios se utiliza para comparar los predictores de CASP16. 

La Figura 1A ilustra las puntuaciones Z acumuladas de las 20 mejores de 120 predictores de CASP16. Nuestro predictor MULTICOM logró una puntuación Z acumulada de 33,39, ubicándose 4.º, justo después de tres predictores (Yang-Server, Yang, Yang-Multimer) del mismo grupo, el grupo Yang. Si solo se cuenta al mejor predictor de cada grupo, MULTICOM obtuvo el 2.º lugar. Los otros predictores MULTICOM, incluidos MULTICOM_LLM, MULTI- COM_AI y MULTICOM_human, quedaron 10.º, 17.º y 19.º, con puntuaciones Z de 30,98, 28,78 y 28,21, respectivamente. Cabe destacar que el predictor estándar AlphaFold3 del grupo de Elofsson, AF3-server, quedó 29.º con una puntuación Z acumulada de 25,71, lo que indica que los predictores MULTICOM lograron mejoras sustanciales sobre AlphaFold3 estándar. En este trabajo, 

Notablemente, MULTICOM logró la puntuación Z más alta de 3.81 para el dominio T1267s1-D1 (Fig. 2A), que es el primer dominio de la subunidad T1267s1 del objetivo complejo H1267 (estequiometría: A2B2, una proteína XauSPARDA). La estructura de este dominio se obtuvo del modelo estructural complejo previsto para H1267 por el módulo de predicción de estructuras complejas MULTICOM4 utilizando AlphaFold3 con muestreo extenso de modelos. La alta calidad de predicción para T1267s1-D1 puede deberse a que su conformación estructural altamente estable y cohesionada fue capturada bien por el extenso muestreo de modelos. En contraste, la puntuación Z para el segundo dominio de la misma subunidad, T1267s1-D2, es -0.01, porque está involucrado en interacciones entre cadenas que no fueron correctamente predichas en el modelo del complejo proteico. Un ejemplo opuesto es T1237-D1 (puntuación Z = 1.23, Fig. 2B), una subunidad del complejo tetramerico T1237o (estequiometría: A4). La estructura de este dominio se obtuvo del complejo de alta calidad predicho por el predictor AlphaFold3 dentro del módulo de predicción de estructuras complejas MULTICOM. Estos ejemplos demuestran que la precisión de la predicción estructural para subunidades individuales en un objetivo complejo depende en gran medida de la calidad de las estructuras complejas predichas. 

Para el objetivo monomérico T1210-D1 (puntuación Z = 1,16, Fig. 2C), MULTICOM presentó un modelo top-1 generado por AlphaFold3 que alcanzó un GDT-TS de 0,724, el más alto entre todos los grupos participantes, superando al modelo interno top-1 de AlphaFold2 (GDT-TS = 0,636). El éxito en este objetivo se debe al uso de AlphaFold3 con muestreo extenso de modelos. 

T1257-D1 (puntuación Z = 1,10, Fig. 2E), una subunidad del complejo trímero T1257o (estequiometría: A3), presentó un caso de modelado particularmente desafiante porque T1257 es una estructura similar a un filamento largo, pero AlphaFold3 tiende a doblarlo para que interactúen el N- y C-terminal. Para superar este problema, se aplicó una estrategia de dividir y conquistar para dividir la estructura complejo en tres regiones superpuestas, cada una de las cuales se predijo de forma independiente usando AlphaFold3. Los modelos de las tres regiones se combinaron luego para formar un modelo complejo lineal de longitud completa al superponerse en las regiones superpuestas. Produjo un modelo top-1 de alta calidad tanto para el complejo como para su subunidad. 

Aunque MULTICOM obtuvo un rendimiento por encima de la media en la mayoría de los dominios, tuvo un rendimiento inferior en algunos dominios con puntuaciones Z negativas, como T1266-D1 (–0,09), T1271s7-D1 (–0,15), T1228-D1 (–0,28), T1235-D1 (–0,31), T1207-D1 (–0,32), T1271s3-D1 (–0,35), T1271s5-D2 (–0,35), T1239-D1 (–0,42), T1218-D2 (–0,55), T1226-D1 (–0,59), T1295-D1 (–0,60), T1271s8-D1 (–0,61), T1295-D2 (–0,92), T1239-D4 (–0,93), T1220s1-D1 (–0,97), T1218-D3 (–1,34) y T1218-D1 (–2,36) por varias razones. 

Para T1266-D1 (puntuación Z = –0,09), un objetivo monomérico de cadena simple, la puntuación GDT-TS del modelo top-1 de MULTICOM generado por AlphaFold3 fue 0,797, lo que está por debajo del promedio. Sin embargo, al usar AlphaFold2 con un MSA basado en dominios, MULTICOM pudo generar un modelo sustancialmente mejor. Específicamente, el objetivo se dividió en dos regiones (residuos 1–188 y 189–366) que se predecían como dos dominios separados. Se generaron MSAs para ellas por separado y luego se concatenaron como un MSA de longitud completa para que AlphaFold2 generara un modelo de mayor precisión con GDT-TS 0,877. Este ejemplo demuestra que la generación de MSAs basada en dominios puede generar mejores MSAs para algunos objetivos para mejorar la predicción de la estructura terciaria de AlphaFold, cuando la generación de MSA de longitud completa no cubre algunas regiones de un objetivo. Sin embargo, este modelo de alta calidad no fue seleccionado como la predicción n.º 1 por MULTICOM. 

Communications Biology | (2025) 8:1587 

2 

Artículo 

https://doi.org/10.1038/s42003-025-08960-6 

**==> picture [483 x 405] intentionally omitted <==**

**----- Start of picture text -----**<br>
(GY) Top 20 Predi Grupos R ked por C ve Z-score a través de 75 dominios<br>40.93<br>39.39<br>35.62<br>“a wn 33.39 32.71<br>a <<br>[[ wv<br>a <<br>wv —<br>= =)<br>ugg Puy, Moy; np<br>“I-51<br>Wing Sua, oy,<br>Xx Lin<br>(B) Z-scores de GDT-TS para MULTICOM para los 75 dominios<br>Métricas<br>=== Promedio Z-score<br>MULTICOM<br>3<br>2<br>21008-71<br>0 a<br>2<br>1a-0ITILr €d-6€TIL I 1d-6STLTILI F [ I F I I I €d-S6TIL F I 1d-66C1LI r 1d-69T1L1d-99T1L1d-L0TILF [ I<br>**----- End of picture text -----**<br>


Fig. 1 | El rendimiento general de los 20 mejores de 120 predictores de CASP16 y el rendimiento detallado de MULTICOM en 75 dominios únicos. A Las puntuaciones Z acumuladas de los 20 mejores predictores. El predictor estándar AlphaFold3 (AF3- 

servidor) ejecutado por el grupo de Elofsson ocupó el puesto 29 con una puntuación Z acumulada de 25,71 (no mostrado); B La puntuación Z de la mejor predicción de MULTICOM para cada uno de los 75 dominios. 

Para T1235-D1 (puntuación Z = –0,41), una subunidad de T1235o (estequiometría: A6), el mejor modelo extraído de la estructura compleja predicha por AlphaFold3 fue de menor calidad que uno generado por AlphaFold2-Multimer. Un problema similar ocurrió para los dominios T1295-D1 (puntuación Z = –0,60) y T1295-D2 (puntuación Z = –0,92), extraídos del objetivo octamérico T1295o (estequiometría: A8), los modelos basados en AlphaFold3 fueron de menor calidad en comparación con los construidos usando AlphaFold2-Multimer con MSAs diversos, pero fueron seleccionados como la mejor predicción. De igual manera, para T1220s1-D1 (puntuación Z = –0,97), una subunidad de H1220 (estequiometría: A1B4), el mejor modelo extraído de la estructura compleja predicha por AlphaFold3 con alta confianza predicha (por ejemplo, 0,594) tenía menor calidad que la estructura extraída de una predicción de AlphaFold2-Multimer con mucha menor confianza (por ejemplo, 0,384). Estos tres ejemplos significan la dificultad de clasificar los modelos de AlphaFold2 y AlphaFold3 cuando no son consistentes. 

Para T1207-D1 (objetivo monomérico de cadena única, Z-score = –0.32), no logró predecir las interacciones hélice-hélice dentro de la región C-terminal ni su interacción con otras regiones. En su lugar, predijo la región C-terminal como una hélice larga y extendida, lo que resultó en un modelo mediocre (GDT-TS = 0.564, Fig. 2D). Aunque el MSA de longitud completa que se utilizó para construir esta estructura contiene 1310 secuencias, la profundidad de alineamiento para los últimos 30 residuos del C-terminal es mucho menor, variando desde 175 secuencias alineadas hasta tan solo 

2. La profundidad media en esta región es solo de 84,4. La cobertura superficial cerca del C-terminal probablemente causó la predicción incorrecta para la región. 

Se predijeron diferentes conformaciones estructurales para T1226-D1 (puntuación Z = –0,59) aunque tiene un MSA profundo. Pero una conformación muy sobrerrepresentada pero incorrecta fue seleccionada como la mejor predicción, mientras que la conformación correcta apareció solo en un pequeño número de modelos generados por AlphaFold3 y no fue seleccionada. Este ejemplo resalta el desafío de seleccionar buenos modelos cuando solo hay unos pocos en el conjunto de modelos. El error del mejor modelo para T1226-D1 es similar al del mejor modelo de T1207-D1, ambos predijeron incorrectamente la región helicoidal C-terminal como una hélice extendida en lugar de una estructura helicoidal plegada. 

Para T1218-D1 (Z-score = –2.36), T1218-D2 (Z-score = –0.55) y T1218-D3 (Z-score = –1.34), los tres dominios de la subunidad T1218 en el complejo T1218o, la calidad de sus modelos estructurales es relativamente baja debido a la combinación de la estructura del complejo predicha por AlphaFold3 y el modelo de complejo construido a partir de una plantilla de complejo significativa (código PDB: 4W8J) usando Modeller15. La combinación mejoró la calidad del modelo de complejo para T1218o pero degradó la calidad de los dominios individuales en las subunidades del complejo. Este ejemplo es consistente con la observación de que la predicción basada en AlphaFold para dominios individuales suele ser más precisa que la modelización basada en plantillas. 

Communications Biology | (2025) 8:1587 

3 

Artículo 

https://doi.org/10.1038/s42003-025-08960-6 

**==> picture [481 x 393] intentionally omitted <==**

Fig. 2 | La comparación estructural entre las estructuras nativas (verde) y los modelos top-1 enviados por MULTICOM (azul). A T1267s1-D1 (GDT-TS = 0.878), B T1237-D1 (GDT-TS = 0.905), C T1210-D1 (GDT-TS = 0.724), D T1207-D1 (GDT-TS = 0.564), E T1257-D1 (GDT-TS = 0.780). 

Algunos dominios en tres complejos proteína-ácido nucleico, incluido T1228-D1 (puntuación Z = –0,28) de M1228 (estequiometría: A4B2C2D2E2), T1239-D1 (puntuación Z = –0,42), T1239-D4 (puntuación Z = –0,93) de M1239 (estequiometría: A4B2C2D2E2) y T1271s3-D1 (puntuación Z = –0,35), T1271s5-D2 (puntuación Z = –0,35), T1271s7-D1 (puntuación Z = –0,15) y T1271s8-D1 (puntuación Z = –0,60) de M1271 (estequiometría: A1B1C1D1E1F2G2H1I1J5R1) tienen predicciones top-1 de baja calidad. La falla se debió principalmente a la predicción no exitosa de las regiones de estos dominios en los modelos de estructura de complejos. En particular, M1271 tiene más de 5000 residuos, excediendo el límite de longitud de AlphaFold3. Se dividió en dos subcomplejos cuyas estructuras se predecían por separado y luego se combinaron. Sin embargo, AlphaFold3 no pudo predecir algunas interacciones entre cadenas en los subcomplejos que influyen en las estructuras de los dominios. Además, algunos subunidades como T1271s5 y T1271s7 contienen residuos desordenados, lo que puede complicar aún más la predicción. 

La Figura 3 resume las puntuaciones TM de los modelos top-1 y de los mejores de top-5 presentados por MULTICOM para los 84 dominios. La puntuación TM promedio fue 0.902 para los modelos top-1 y 0.922 para los modelos best-of-top-5. Como se muestra en Fig. 3A, las predicciones top-1 de MULTICOM alcanzaron una calidad casi nativa (TM-score>0.9) para 62 dominios (73.8%) y pliegues correctos en general (TM-score>0.5) para 82 dominios (97.6%). En solo dos dominios, T1226-D1 y T1271s8-D1, las predicciones top-1 tuvieron puntuaciones TM por debajo de 0.5 debido al fallo de la selección de modelos, mientras que las predicciones best-of-top-5 para ellos tenían TM-score por encima de 0.5. 

Fig. 3B representa las puntuaciones TM de los modelos top-1 frente a los mejores de top-5 modelos enviados por MULTICOM. Todos los mejores de top-5 modelos para los 84 dominios tienen un pliegue correcto (TM-score > 0.5). Para la mayoría de dominios, las puntuaciones TM de las predicciones top-1 son bastante similares a las de las predicciones best-of-top-5, lo que indica que el método de selección de modelos funcionó bien para ellos. Sin embargo, para cuatro dominios (T1226-D1, T1271s8-D1, T1239v1-D3 y T1245s2-D1) destacados en amarillo, la puntuación del mejor de top-5 predicción es sustancialmente más alta que la predicción top-1 (la diferencia de puntuación > 0.1), lo que indica que MULTICOM no logró seleccionar modelos de alta calidad como top-1 para estos dominios. En el caso de T1226-D1, el modelo top-1 tenía una TM-score de 0.378, mientras que una formación alternativa y rara presente en un modelo con TM-score de 0.725 fue incluida en los top 5 modelos. El modelo minoritario generado por el muestreo extensivo de modelos plegó correctamente la región helicoidal en el extremo C y su interacción a larga distancia con otras regiones, mientras que los modelos mayoritarios predijeron la región terminal C como una hélice larga y extendida sin interacción con otras regiones. Para T1271s8-D1, un dominio de una subunidad de un complejo muy grande objetivo M1271, el mejor de top-5 provino de un modelo de complejo parcial de M1271 predicho por AlphaFold3, que fue diferente del modelo parcial de complejo que contenía el top-1. Este ejemplo demuestra que cuando un modelo de complejo (p. ej., M1271) es demasiado grande, dividirlo en diferentes subcomplejos para construir modelos puede ayudar a generar mejores estructuras para algunas subunidades. Considerar diferentes opciones aumenta la probabilidad de incluir buenos modelos en las predicciones de los 5 primeros. 

Communications Biology | (2025) 8:1587 

4 

Artículo 

https://doi.org/10.1038/s42003-025-08960-6 

**==> picture [497 x 361] intentionally omitted <==**

**----- Start of picture text -----**<br>
(A) TM-score por dominio del modelo top-1 enviado por MULTICOM<br>1.00 Cerca de nativo (0.9)<br>0.75<br>)<br>0.50<br>0.25<br>0.00<br>1d-90T1L1a-6LT1L TA-TAGETIL1a-9s1LTILTA-TA8TTIL TA-TA6ETIL€d-S6TILTA-1sL9TIL 1d-9921L £A-TA6ETIL1d-6STLTIL €d-TA8TTILPA-TAGETIL1d-L0T1L<br>m ~~jo) = = =} g < Q g 5 = o “= = = wn Q =} = 7) oO Q E = 8 = 1 — < E oO [+ ? 2 w = Q ° Q A]<br>— 3 3 [23 \ \ \ \<br>= 1 3 Qo<br>\ © Qe 4<br>oc oNS ~~ wvo wy=3 =]wy \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ = Q a _\ \ \ \ \ Ye\ k = oN o ~ @ [=]\ \ \ \ \ \ \ \ \ | \ \ \ LLORA\ \ \ \  \ \ \ \ \ \] a \ 9 4<br>\ [\ \ WS] vo =] a Ie = © &= 2 pi g<br>**----- End of picture text -----**<br>


Fig. 3 | Las puntuaciones TM de los modelos top-1 y mejores de los cinco mejores presentados por MULTICOM para los 84 dominios. A Las puntuaciones TM de los modelos top-1 para los 84 dominios. B Puntuaciones TM de los modelos top-1 frente a las puntuaciones TM de los mejores de los cinco mejores modelos en los 84 dominios. 

En T1239v1-D3, el mejor de los cinco mejores modelos y el modelo top-1 fueron seleccionados de dos clústeres de modelos diferentes. Para T1245s2-D1, una subunidad del complejo H1245 (estequiometría: A1B1), el modelo top-1 fue predicho por AlphaFold3, que fue mucho peor que el mejor de los cinco mejores modelos predicho por AlphaFold2-Multimer usando MSAs basados en alineamiento estructural. Los resultados demuestran que clasificar el mejor modelo como número 1 para objetivos difíciles sigue siendo muy desafiante, pero incluir modelos alternativos en el top 5 es un enfoque efectivo para aumentar la probabilidad de obtener al menos un buen modelo en las cinco mejores predicciones. 

## Comparación de rendimiento entre MULTICOM y AF3-server 

La Figura 4 compara las puntuaciones TM de los modelos top-1 y mejores de los cinco mejores de MULTICOM y el predictor estándar AlphaFold3 (AF3-server) en 84 dominios. La Figura 4A muestra las puntuaciones TM de los modelos top-1 de los dos métodos, mientras que la Figura 4B muestra las puntuaciones TM de los mejores de los cinco mejores modelos de los dos métodos. Es importante señalar que AF3-server generó exactamente cinco modelos (por ejemplo, un trabajo) usando AlphaFold3-server para la mayoría de los objetivos, lo cual es mucho menos que el número de modelos generados por MULTICOM. 

En cuanto a la calidad del modelo top-1, MULTICOM logró una puntuación TM promedio ligeramente superior (0.902) en comparación con AF3-server (0.891). Aunque esta diferencia no fue estadísticamente significativa según una prueba de rango con signo de Wilcoxon unilateral (p = 0.08), MULTICOM mostró un rendimiento más fuerte en 6 dominios (es decir, T1271s8-D1, T1257-D1, T1267s1-D1, T1271s4-D1, T1239v2-D3 y T1284-D1), con una diferencia de puntuación TM mayor a 0.1, mientras que AF3-server tuvo un desempeño mucho mejor en 3 dominios: T1271s5-D2, T1295-D2 y T1218-D2. 

Para T1257-D1, el rendimiento superior de MULTICOM se atribuye al uso de una estrategia de dividir y conquistar con AlphaFold3 que generó una conformación alargada, en contraste con la conformación doblada predicha por el AlphaFold3 predeterminado, como se describió anteriormente. Para T1267s1-D1, T1284-D1 y T1239v2-D3, la ventaja de MULTICOM se debe al muestreo extensivo usando AlphaFold3 y/o el agrupamiento de modelos para mejorar la selección de modelos. 

Para los tres dominios derivados del mismo complejo grande M1271 (es decir, T1271s8-D1, T1271s4-D1, T1271s5-D2), MULTICOM tuvo un mejor desempeño en T1271s8-D1 y T1271s4-D1, mientras que AF3-server tuvo un mejor desempeño en T1271s5-D2. La diferencia puede deberse en parte a los diferentes subcomplejos utilizados por los dos métodos para generar modelos estructurales. 

En el caso de T1218-D2, el peor desempeño de MULTICOM se debe a su uso de modelado basado en plantillas, como se describió anteriormente. Para T1295-D2, AF3-server tuvo un mejor desempeño que MULTICOM, lo que indica que el muestreo extensivo de modelos no siempre conduce a mejores modelos top-1 porque generar más modelos no significa que los buenos modelos puedan clasificarse como número 1. 

En cuanto a los mejores de los cinco mejores modelos, la brecha de rendimiento entre MULTICOM y AF3-server se amplió (una puntuación TM promedio de 0.922 de MULTICOM frente a 0.904 de AF3-server). La prueba de rango con signo de Wilcoxon unilateral confirma que esta diferencia es estadísticamente significativa (p = 1.491e–05). MULTICOM produjo modelos sustancialmente mejores para 8 dominios, mientras que AF3-server tuvo un desempeño mucho mejor en 2 dominios. Además de los 4 dominios donde MULTICOM ya superó a AF3-server en cuanto a la calidad del modelo top-1 (es decir, T1257-D1, T1267s1-D1, T1239v2-D3 y T1284-D1), tuvo un desempeño mucho mejor que AF3-server en otros cuatro dominios (T1226-D1, T1239v1-D3, T1245s2-D1 y T1295-D1 en cuanto a los mejores de los cinco mejores modelos). 

Communications Biology | (2025) 8:1587 

5 

Artículo 

https://doi.org/10.1038/s42003-025-08960-6 

**==> picture [483 x 239] intentionally omitted <==**

**----- Start of picture text -----**<br>
(A) Comparación entre la TM-score de los modelos Top-1 (B) Comparación entre la TM-score de los modelos mejor de los 5 mejores<br>desde AF3-server y MULTICOM desde AF3-server y MULTICOM<br>1,00 T1257-D1 1,00<br>» T124552-D<br>T1239v2-D301 7 1 él D2<br>rad<br>T1295-D2 T4295-D1 T1295-D2<br>0,75 2716,02 0,75 T1226-D1¥<br>»<br>como<br>==} 4 [=] I]=<br>ne<br>Si E050<br>= 2<br>5 =<br>® T1271s8-D1 ry .<br>0.25 7 0.25<br>000 000<br>0.00 0.25 0.50 0.75 1.00 0.00 0.25 0.50 0.75 1.00<br>AF3-server AF3-server<br>**----- End of picture text -----**<br>


Fig. 4 | Comparación de TM-score de cabeza a cabeza entre MULTICOM y AF3-server en 84 dominios de proteínas. A Modelos Top-1 y B mejores de Top-5 modelos. 

**==> picture [483 x 176] intentionally omitted <==**

**----- Start of picture text -----**<br>
mmm Top-1 de Inhouse_AF2 mm Top-1 de AF3-server mmm Top-1 de Inhouse_AF3<br>Mejor de Top-5 de Inhouse_AF2 Mejor de Top-5 de AF3-server ~~ Mejor de Top-5 de Inhouse_AF3<br>1.0 0.060-97 0:960.960.96 0.991.00 1.00 0.99 1.00 1.00 0.98 0.98 0.99<br>0.908188<br>0.870.870.87 850.84<br>0.8<br>2 0.62 06 4 0.65<br>0.6<br>[a]<br>0.4<br>0.2<br>0.0<br>T1207-D1 T1210-D1 T1226-D1 T1231-D1 T1243-D1 T1246-D1 T1266-D1 T1274-D1 T1278-D1 T1280-D1 T1284-D1 T1299-D1<br>**----- End of picture text -----**<br>


Fig. 5 | Comparación del rendimiento GDT-TS entre el AlphaFold2 interno, el predictor AlphaFold3 interno y el servidor AF3 de CASP16 para los 12 objetivos de monómeros de cadena única. Los gráficos muestran los modelos top-1 y mejores de Top-5 generados por nuestro AlphaFold2 interno, nuestros predictores AlphaFold3 internos y AF3-server. 

calidad del modelo top-5. Para T1226-D1, una conformación alternativa que se incluyó en los top5 modelos tuvo una puntuación significativamente más alta que los modelos presentados por AF3-server. En el caso de T1239v1-D3 (un objetivo de multi conformación), el clustering de modelos efectivo facilitó la selección de un modelo de mayor calidad. Para T1245s2-D1, la estructura extraída del modelo complejo predicho por AlphaFold2-Multimer que se incluyó en los 5 mejores modelos tuvo mejor calidad que la de AlphaFold3. Una observación similar se aplica a T1295-D1, donde el modelo basado en AlphaFold2-Multimer superó a AlphaFold3. Sin embargo, para T1295-D2 y T1271s8-D1, AF3-server aún superó a MULTICOM, consistente con su ventaja en la calidad del modelo top-1 para esos dominios. 

en la Fig. 5. En esta comparación, los 5 modelos top para AlphaFold2 se seleccionaron según sus puntuaciones plDDT previstas, mientras que se utilizaron las puntuaciones de clasificación de AlphaFold3 para seleccionar sus 5 modelos superiores. 

La puntuación media GDT-TS de los modelos top-1 para el AlphaFold2 interno fue 0.825, para AF3-server es 0.830 y para el AlphaFold3 interno es 0.838. La media de best-of-top-5 GDT-TS para el AlphaFold2 interno es 0.830, para AF3-server es 0.840 y para el AlphaFold3 interno es 0.870. Los resultados muestran que el AlphaFold3 interno obtuvo mejor rendimiento que AF3-server, mientras que AF3-server superó ligeramente a AlphaFold2. AF3-server muestreó un número mucho menor de modelos estructurales (p. ej., cinco modelos) que el AlphaFold2 interno (cientos/miles de modelos) pero aún así lo superó claramente demuestra que AlphaFold3 rinde mejor que AlphaFold2 en la predicción de la estructura terciaria de proteínas de cadena simple. 

## Comparación de AlphaFold2 y AlphaFold3 en objetivos de monómeros 

Para eliminar el impacto de la predicción de estructuras complejas en la predicción de estructuras terciarias, comparamos nuestro AlphaFold2 interno, nuestro AlphaFold3 interno y el servidor AF3 de CASP16 en 12 objetivos de monómeros de CASP16 que no forman parte de ningún objetivo multimono. Se ilustran las puntuaciones GDT-TS de los modelos top-1 y de los mejores de Top-5 de los tres métodos para los 12 dominios. 

En cuanto a las predicciones top-1, el AlphaFold3 interno se desempeñó de manera similar al AlphaFold2 interno en 9 de los 12 dominios. Para dos dominios (T1210-D1 y T1231-D1), el AlphaFold3 interno superó significativamente al AlphaFold2 interno (diferencia de puntuación GDT-TS > 0,05), mientras que se desempeñó sustancialmente peor que el AlphaFold2 interno en uno. 

Communications Biology | (2025) 8:1587 

6 

Artículo 

https://doi.org/10.1038/s42003-025-08960-6 

**==> picture [483 x 75] intentionally omitted <==**

**----- Start of picture text -----**<br>
(A)<br>**----- End of picture text -----**<br>


Fig. 6 | Comparación de estructuras predichas para el objetivo T1226-D1. A Estructura nativa; B mejor modelo entre las predicciones top-5 del AlphaFold3 interno (GDT-TS = 0.650); C modelo top-1 del AlphaFold3 interno (GDT-TS = 0.336); D modelo top-1 del AlphaFold2 interno (GDT-TS = 0.334). El mejor de los 5 primeros. 

el modelo del AlphaFold3 interno predijo correctamente el plegamiento de las hélices C-terminales y su interacción a larga distancia con otras regiones, mientras que los otros modelos no. 

**==> picture [483 x 207] intentionally omitted <==**

**----- Start of picture text -----**<br>
ColabFold DeepMSA_dMSA AF2 por defecto ESM-MSA DHR<br>GDT-TS<br>T1207-D1 T1210-D1 T1226-D1 T1231-D1 T1243-D1 T1246-D1 T1266-D1 T1274-D1 T1278-D1 T1280-D1 T1284-D1 T1299-D1<br>**----- End of picture text -----**<br>


Fig. 7 | Comparación del rendimiento de GDT-TS para modelos top-1 generados usando diferentes fuentes de MSA. Cada MSA fue evaluada con AlphaFold2 bajo configuraciones de entrada idénticas. 

dominio (T1266-D1). Como se describió antes, el modelo in-house de AlphaFold3 para T1210-D1 es el mejor entre todos los modelos CASP16 enviados por todos los predictores CASP16, lo que indica que una muestreo extenso de modelos con AlphaFold3 es esencial para obtener modelos de alta calidad para este objetivo. Es notable que el MSA interno para T1231-D1 era superficial y tenía menos de 20 secuencias, lo que indica que AlphaFold3 rindió mejor que AlphaFold2 para algunos objetivos con información evolutiva limitada. AlphaFold2 interno rindió mejor en T1266-D1 porque utilizó el MSA basado en dominio mejorado, mientras que AlphaFold3 solo pudo usar el MSA por defecto provisto por el servidor web público de AlphaFold3 de DeepMind. 

En lo que respecta a los modelos mejor de los primeros cinco, hay una única diferencia importante respecto a la comparación en términos de modelos top-1. Para T1226-D1 (Fig. 6) —el objetivo más difícil para el cual los modelos top-1 de AlphaFold2 y AlphaFold3 tenían una puntuación GDT-TS baja entre 0.33 y 0.35, pero el modelo best-of-top-5 del AlphaFold3 interno (Fig. 6B) tuvo una puntuación GDT-TS de 0.65, notablemente más alta que la del modelo top-1 del AlphaFold3 interno (Fig. 6C) y la del modelo top-1 del AlphaFold2 interno (Fig. 6D). Este caso resalta la ventaja de AlphaFold3 sobre AlphaFold2 en ciertos objetivos desafiantes, donde AlphaFold3 puede generar modelos con plegamientos correctos mediante muestreo extenso de modelos, pero AlphaFold2 falla. Sin embargo, el mejor modelo no se clasificó en la cima parcialmente porque era un modelo minoritario en la pool de modelos. En este objetivo, el modelo best-of-top-5 del AlphaFold3 interno también tiene una puntuación GDT-TS mucho más alta que la del AF3-servidor, lo que indica que es necesario un muestreo extenso de modelos para que AlphaFold3 genere buenos modelos para este objetivo difícil. 

AlphaFold3, AlphaFold2 interno y AF3-servidor) tenían alta calidad de esqueleto (GDT-TS > 0.70). La localización de cadenas laterales se midió usando la métrica GDC_SC (Cálculo Global de Distancia para cadenas laterales). Valores mayores indican mayor precisión. Los resultados se muestran en la Figura Suplementaria Fig. S1. El AlphaFold3 interno consiguió la media más alta de GDC_SC tanto para top-1 (0.644) como para best-of-top-5 (0.647), seguido por el AF3-servidor (0.631/0.638) y el AlphaFold2 interno (0.618/0.620). Las comparaciones por objetivo muestran que AlphaFold3 superó sustancialmente a AlphaFold2 en T1231-D1 y T1274-D1 (mejoras de GDC_SC > 0.07), mientras que AlphaFold2 superó ligeramente a AlphaFold3 en T1266-D1. En general, AlphaFold3 puede generar modelos con mayor precisión de las cadenas laterales que AlphaFold2 para objetivos con una estructura de esqueleto de alta calidad. 

## Rendimiento de diferentes MSAs para la generación de modelos 

Para investigar el impacto de diferentes alineamientos de secuencias múltiples (MSA) en la precisión de la predicción de estructuras, evaluamos la precisión de los modelos estructurales generados por el AlphaFold2 interno usando diferentes fuentes de MSA a lo largo de los 12 objetivos de monómeros de cadena única. Todos los modelos se generaron usando plantillas estructurales idénticas y los mismos parámetros de modelado (es decir, num_recycle y num_ensemble) para aislar el efecto de los MSAs. Los tipos de MSA evaluados incluyen ColabFoldMSA proporcionado por CASP16 y curado por Steinegger Group, DeepMSA_dMSA, DeepMSA_qMSA, Default_AF2, ESM-MSA y DHR (ver definiciones de los MSAs en la Sección “Muestreo de MSA de longitud completa”) como se muestra en la Fig. 7. 

Para evaluar aún más la precisión de las cadenas laterales, analizamos nueve objetivos de monómero para los cuales los modelos de rango superior generados por cada método (internos) 

Cada MSA anterior fue utilizada por AlphaFold2 para generar la misma cantidad de modelos estructurales para los 12 objetivos de monómeros de cadena única durante CASP16. El modelo top-1 fue seleccionado por el plDDT de AlphaFold2. 

Communications Biology | (2025) 8:1587 

7 

Artículo 

https://doi.org/10.1038/s42003-025-08960-6 

**==> picture [65 x 3] intentionally omitted <==**

**----- Start of picture text -----**<br>
i i i<br>**----- End of picture text -----**<br>


**==> picture [60 x 36] intentionally omitted <==**

**----- Start of picture text -----**<br>
H<br>i<br>**----- End of picture text -----**<br>


Fig. 8 | Comparación de estructuras previstas para el objetivo T1266-D1 utilizando MSA de longitud completa y MSAs basados en dominios. A Estructura nativa; B MSAs de longitud completa, que incluyen ColabFold, DeepMSA_qMSA, DeepMSA_dMSA, Default_AF2, ESM-MSA y 

score. Las puntuaciones medias GDT-TS de estos modelos top-1 para cada MSA fueron las siguientes: ColabFold (0.831), DeepMSA_dMSA (0.820), Default_AF2 (0.790), ESM-MSA (0.793) y DHR (0.830). DeepMSA_qMSA se utilizaron para generar modelos estructurales para 11 objetivos durante CASP16. Su puntuación media de GDT-TS sobre los 11 objetivos es 0.813. En promedio, ColabFold y DHR produjeron los modelos más precisos entre los métodos de MSA probados. Sin embargo, ningún MSA siempre obtuvo mejor rendimiento que otros MSAs para todos los objetivos, lo que indica que es útil usarlos para generar un conjunto diverso de modelos. 

Para complementar la precisión a nivel de esqueleto, también evaluamos la precisión de la posición de las cadenas laterales de los modelos estructurales generados a partir de diferentes MSAs utilizando la métrica GDC_SC (Figura Suplementaria Fig. S2). Entre los siete objetivos con alta precisión de esqueleto, las puntuaciones medias fueron: ColabFold (0.657), DeepMSA_dMSA (0.644), DeepMSA_qMSA (0.647), Default_AF2 (0.657), ESM-MSA (0.647) y DHR (0.650). Aunque las diferencias son pequeñas, las alineaciones de ColabFold, Default_AF2 y DHR tendieron a ofrecer una precisión de cadena lateral ligeramente mayor para los objetivos. 

Para ilustrar mejor el efecto de la calidad de MSA en la precisión de la predicción, examinamos dos casos representativos: T1231-D1 y T1266-D1, donde ColabFold y DHRMSAs superaron notablemente al MSA predeterminado AlphaFold2 (Default_AF2). Para T1231-D1, todos los MSAs contenían menos de 20 secuencias, y sin embargo, la GDT-TS de los modelos top-1 varió significativamente entre diferentes MSAs. Los modelos generados usando Default_AF2 y ESM-MSA mostraron un desempeño notablemente peor que aquellos que usaron ColabFold, DeepMSA_dMSA, DeepMSA_qMSA y DHR, lo que sugiere que estos MSAs son de mayor calidad a pesar de ser poco profundos. Para T1266-D1, el impacto de la fuente de MSA también es notable. Los modelos de DeepMSA_qMSA, Default_AF2 y ESM-MSA adoptaron consistentemente la misma baja calidad 

DHR; C MSAs basadas en dominios con diferentes métodos de segmentación de dominios: DomainParser, HHsearch, UniDoc y Manual. 

confomeración, resultando en puntuaciones GDT-TS significativamente más bajas en comparación con las de ColabFold, DeepMSA_dMSA y DHR. 

Curiosamente, aunque T1266-D1 se clasifica formalmente como una unidad de evaluación de un dominio por los evaluadores y organizadores de CASP16, en realidad tiene dos dominios estructurales (Fig. 8A) (un dominio beta/alpha y un dominio helicoidal). Nuestro enfoque de generación de MSA basado en dominios que genera MSA para dominios individuales por separado y luego los combina con MSAs de longitud completa también mejoró significativamente la calidad del modelo. Como se muestra en la Fig. 8B, el modelo predicho usando el MSA de longitud completa predeterminado (Default_AF2) tiene un GDT-TS de solo 0.570. El error principal ocurre en el dominio C-terminal y en la región entre dominios, dando lugar a un dominio C-terminal parcialmente mal plegado y una orientación de dominio incorrecta, posiblemente debido a la falta de señales coevolutivas en la MSA. 

En contraste, las MSAs específicas de dominio generadas usando herramientas de segmentación de dominios como DomainParser, HHsearch, UniDoc y anotación de dominio manual (ver Sección “Construcción de MSA basada en dominios”) dieron lugar a modelos sustancialmente mejores que la MSA de longitud completa, con puntuaciones GDT-TS que oscilan entre 0.859 y 0.878 (Fig. 8C). Estos resultados indican que para objetivos reales multi-dominio, el muestreo de MSAs sensible al dominio puede mejorar la calidad de las MSAs y de los modelos estructurales, y la calidad de la MSA no es sensible a las herramientas específicas de segmentación de dominios utilizadas. Este ejemplo demuestra que la ingeniería de MSA es importante para generar buenas predicciones para objetivos difíciles multi-dominio. 

Finalmente, como se muestra en la Fig. 7, todas las MSAs fallaron en el dominio T1226-D1, aunque son profundas. Como se discutió anteriormente, solo AlphaFold3 con muestreo extenso de modelos fue capaz de generar un modelo con la estructura correcta para él. Esto demuestra que el muestreo extenso de modelos puede ser capaz de explorar un amplio 

Communications Biology | (2025) 8:1587 

8 

Artículo 

https://doi.org/10.1038/s42003-025-08960-6 

**==> picture [483 x 202] intentionally omitted <==**

**----- Start of picture text -----**<br>
Método<br>pIDDT (prom:)<br>PSS (prom:)<br>GATE (prom:)<br>EnQA (prom:)<br>GCPNet-EMA (prom:)<br>MULTICOM (prom:)<br>Mejor (prom:)<br>GDT-TS<br>T1207-D1 T1226-D1 T1210-D1 T1243-D1 T1284-D1 T1266-D1 T1246-D1 T1299-D1 T1231-D1 T1280-D1 T1278-D1 T1274-D1<br>Objetivo<br>**----- End of picture text -----**<br>


Fig. 9 | Puntuaciones GDT-TS de los modelos top-1 seleccionados por diferentes métodos de QA en 12 objetivos de monómero de cadena simple. Los cinco métodos de QA incluyen AlphaFold2 plDDT, puntuación de similitud por pares (PSS), GATE, EnQA y GCPNet-EMA. MULTICOM representa el resultado de los modelos top-1 finales enviados por el 

predictor MULTICOM, que integró los múltiples métodos de QA. Mejor (la línea virtual) representa el límite superior (más alto) del GDT-TS en el conjunto de modelos para cada objetivo. 

espacio estructural para identificar regiones raras con el pliegue correcto. Sin embargo, distinguir modelos correctos de conformación rara de modelos incorrectos pero populares es un desafío. 

## Desempeño de diferentes métodos de evaluación de calidad de modelos (QA) para la selección de modelos 

Comparamos el desempeño de cinco métodos individuales de QA en la selección de modelos top-1 para 12 objetivos de monómero de cadena simple, incluyendo AlphaFold2 plDDT, puntuación de similitud por pares (PSS), GATE, EnQA y GCPNet-EMA utilizados en el sistema MULTICOM, así como MULTICOM en sí. 

agrupar modelos en grupos y comparar las características de diferentes clústeres puede ayudar a seleccionar modelos de clústeres menos populares pero correctos. 

Los hallazgos anteriores destacan que la selección de modelos sigue siendo un desafío importante y que ningún método de QA puede seleccionar consistentemente el mejor modelo en todos los objetivos. Cada método funciona bien en ciertos escenarios, pero puede tener dificultades en otros, dependiendo de las características del objetivo, como la profundidad del MSA, la complejidad estructural o la diversidad de modelos. Por lo tanto, integrar múltiples estrategias de QA, junto con la información sobre la generación y el agrupamiento de modelos, puede ofrecer una solución más robusta para la selección de modelos. 

Las puntuaciones promedio de GDT-TS de los modelos top-1 seleccionados por los cinco métodos individuales de QA son similares, es decir, PSS (0.836), AlphaFold2 plDDT (0.835), GCPNet-EMA (0.833), GATE (0.832) y EnQA (0.832). Sin embargo, hay una diferencia significativa entre PSS y GATE (p = 0.041) así como entre PSS y EnQA (p = 0.032) según la prueba de rango con signo de Wilcoxon unilateral. Como se muestra en la Fig. 9, las puntuaciones GDT-TS de los modelos seleccionados no presentan diferencias o son pequeñas para los cinco métodos de QA en 10 de los 12 objetivos, pero varían mucho para dos objetivos (T1210-D1 y T1231-D1). Para T1210-D1, las puntuaciones GDT-TS de los métodos individuales de QA van de 0.621 (GCPNet-EMA) a 0.684 (GATE), mientras que para T1231-D1, las puntuaciones van de 0.893 (GATE) a 0.970 (AlphaFold2 plDDT). Estas diferencias resaltan la variabilidad en el desempeño de QA para algunos objetivos. Considerando los 12 objetivos, ningún método individual de QA tuvo un desempeño consistentemente mejor que los otros métodos de QA. 

## Discusión 

Los resultados del sistema MULTICOM4 en CASP16 demuestran que integrar un muestreo extenso de modelos con AlphaFold2 y AlphaFold3, múltiples estrategias de ingeniería de MSA y métodos de QA complementarios mejora la predicción de la estructura terciaria respecto a AlphaFold3 o AlphaFold2 por defecto. Notablemente, MULTICOM pudo predecir el pliegue correcto para 82 de 84 dominios (tasa de éxito: 97.6%) en términos de modelos top-1 predichos, y para los 84 dominios (100%) en términos de los mejores de los top-5 modelos, lo que representa una mejora significativa sobre la tasa de éxito del 90.43% de MULTICOM3 en CASP1516. La calidad promedio de las estructuras predichas para los 84 dominios (TM-score promedio = 0.902) alcanzó la precisión de las estructuras experimentales. 

También examinamos los modelos top-1 enviados por MULTICOM. La puntuación promedio de GDT-TS en los 12 objetivos es 0.835, lo cual es comparable con los métodos individuales de QA de mejor desempeño. En T1210-D1, MULTICOM logró la puntuación GDT-TS más alta de 0.724, superando a los cinco métodos de QA, cuyo mejor puntaje fue 0.684 (GATE). Para este objetivo, el modelo top-1 fue seleccionado usando un promedio de la puntuación GATE y la puntuación de clasificación de AlphaFold3, lo que sugiere que combinar métricas de QA complementarias puede mejorar la selección de modelos. Sin embargo, esta estrategia de promediar también tiene limitaciones. En T1266-D1, MULTICOM tuvo un desempeño inferior con un GDT-TS de 0.797, mientras que los cinco métodos de QA lograron puntuaciones superiores a 0.86. En este caso, el promedio pudo haber disminuido el impacto de señales individuales más fuertes, llevando a una selección subóptima. 

Cabe señalar que todos los métodos de QA no lograron seleccionar el buen modelo para T1226-D1 porque los mejores modelos pertenecen a un pequeño clúster en el conjunto de modelos y todos los métodos de QA seleccionaron modelos de calidad mediocre del clúster dominante, como se discutió anteriormente. Este ejemplo sugiere que 

Nuestro experimento muestra que AlphaFold3 superó a AlphaFold2 en la predicción de estructuras terciarias de objetivos de monómero de cadena simple en promedio. Es más adecuado para generar predicciones precisas para algunos objetivos con MSAs poco profundos y limitada información coevolutiva. Por ejemplo, para dos objetivos con MSA poco profundo, T1231-D1 y T1284-D1 (profundidad de MSA <20), AlphaFold3 generó modelos con mayor GDT-TS que AlphaFold2. En el caso de T1231-D1, la elección de las fuentes de MSA impactó significativamente el desempeño de AlphaFold2, pero AlphaFold3 manejó mejor los MSAs poco profundos para generar estructuras precisas. Estos resultados son consistentes con el diseño de AlphaFold3, que enfatiza menos la generación de características de MSA y más la generación de modelos basada en difusión. 

El desempeño de AlphaFold2 para objetivos con MSA poco profundo puede mejorarse mediante ingeniería de MSA, como la generación de MSA basada en dominios. Por ejemplo, para T1266-D1, las predicciones de AlphaFold2 usando MSAs de longitud completa produjeron modelos de baja calidad (GDT-TS = 0.570), mientras que las predicciones usando MSAs basados en dominios lograron una alta puntuación GDT-TS de más de 0.87. Estas mejoras ilustran que AlphaFold2 es sensible a la calidad de los MSAs poco profundos. 

Communications Biology | (2025) 8:1587 

9 

Artículo 

https://doi.org/10.1038/s42003-025-08960-6 

Otra idea clave de CASP16 es la importancia, y también la limitación, del ranking y la selección de modelos. Aunque AlphaFold es capaz de generar estructuras bastante precisas para todos los objetivos de monómeros de CASP16, identificar los modelos correctos de un conjunto de modelos sigue siendo un desafío cuando la mayoría de los modelos del conjunto son de baja calidad y similares. Por ejemplo, para T1226-D1, AlphaFold3 muestreó tanto conformaciones correctas como incorrectas, pero asignó puntuaciones de clasificación interna idénticas a las superiores en los dos clústeres. Como resultado, la estructura incorrecta del clúster predominante se seleccionó como el modelo top-1. Aunque el modelo correcto estaba presente en el conjunto de modelos, estaba subrepresentado y no fue priorizado por ninguno de los métodos de evaluación de calidad (QA) evaluados, incluidos GATE, PSS, EnQA, GCPNet-EMA y plDDT de AlphaFold2. Este ejemplo ilustra una limitación fundamental de las estrategias QA actuales utilizadas en MULTICOM: cuando una conformación incorrecta domina el conjunto de modelos, las herramientas QA avanzadas pueden fallar al identificar la estructura correcta. Algunas inspecciones manuales por parte de expertos humanos pueden ayudar a rescatar el modelo correcto antes de que se desarrollen métodos QA más eficaces para abordar este desafío. 

El desafío de seleccionar los mejores/modelos correctos como predicción número 1 para objetivos difíciles requiere incluir modelos con diferentes conformaciones en las cinco predicciones superiores. En varios casos, como T1226-D1 y T1239v1-D3, modelos de alta calidad no se clasificaron en primer lugar pero fueron incluidos en los cinco mejores modelos. Esto indica que agrupar modelos en grupos y seleccionar un representante de cada grupo es útil para seleccionar cinco modelos para objetivos difíciles. 

Finalmente, la calidad de la predicción de la estructura tridimensional para subunidades de complejos proteicos depende en gran medida de la calidad de las estructuras de complejos previstas. En comparación con la predicción de estructuras de complejos proteicos (cuaternarias), la precisión de la predicción de estructuras tridimensionales es generalmente mayor. Clasificar modelos estructurales tridimensionales es también más fácil que clasificar modelos estructurales de complejos17. Sin embargo, aunque un modelo estructural de complejo previsto no sea preciso, la estructura tridimensional de las unidades individuales, especialmente sus dominios, en el complejo generalmente puede predecirse con precisión mediante AlphaFold2-Multimer y AlphaFold3. 

## Métodos 

## Resumen del módulo de predicción de la estructura tridimensional de MULTICOM4 

MULTICOM4 está construido sobre nuestra versión anterior del sistema de predicción de estructuras de proteínas (MULTICOM3)16,18 y puede predecir tanto la estructura tridimensional de una proteína de una sola cadena (monómero) como la estructura cuaternaria de un complejo proteico de múltiples cadenas (multímero). Dado un objetivo proteico, si es un monómero independiente, MULTICOM4 utiliza su módulo de predicción de estructura tridimensional para predecir su estructura. Sin embargo, si es una subunidad (cadena) de un complejo proteico (multímero), MULTICOM4 llama a su módulo de predicción de estructura cuaternaria para predecir la estructura del complejo primero y luego extraer la estructura tridimensional de la subunidad de la estructura compleja prevista. Este enfoque puede considerar la interacción entre subunidades y, por lo general, producir predicciones de estructura tridimensional más precisas para las subunidades que predecir la estructura tridimensional de cada subunidad por separado. El módulo de predicción cuaternaria de MULTICOM4 ha sido reportado en la ref.14. Aquí, nos centramos en describir su módulo de predicción de estructura tridimensional. 

El módulo de predicción de la estructura tridimensional consta de varias coordinaciones, etapas coordinadas, como se muestra en la Fig.10: alineamiento de múltiples secuencias (MSA) muestreo, construcción de MSA basada en dominios para proteínas multi-dominio, identificación de plantillas estructurales, generación de modelos basada en aprendizaje profundo utilizando tres herramientas (p. ej., AlphaFold2, AlphaFold3, ESMFold7) y selección de modelos basada en un conjunto de métodos de evaluación de calidad de modelos (QA). El diseño modular de MULTICOM4 permite una predicción de estructuras robusta y escalable para una amplia gama de tipos de secuencias y complejidades estructurales. 

## Muestreo de MSA de longitud completa 

El primer paso del módulo de predicción de la estructura tridimensional implica generar un conjunto diverso de alineamientos de múltiples secuencias (MSA) para capturar 

restricciones evolutivas y señales de coevolución. Este proceso de ingeniería de MSA es crítico para la predicción de estructuras. 

La secuencia objetivo completa se busca en varias bases de datos de secuencias de proteínas amplias, que incluyen bases de datos de secuencias de proteínas generales (p. ej., UniRef30_v2023_0219, UniRef90_v2024_0620) y bases de datos de secuencias metagenómicas (p. ej., BFD21,22, MGnify_v2023_0223), usando HHblits24 y JackHMMER25. Estas búsquedas generan MSAs con profundidades y coberturas taxonómicas variables, capturando diversas señales evolutivas a través de secuencias homólogas. Además, la MSA predeterminada utilizada por defecto en AlphaFold2 (denominada Default_AF2), que se genera a partir de BFD, MGnify y UniRef30, también se utiliza. 

Además, MULTICOM4 utiliza dos herramientas adicionales: DeepMSA226 y Dense Homolog Retriever (DHR)27 para generar más MSAs. DeepMSA2 genera MSAs de alta calidad buscando de forma iterativa una combinación de bases de datos de secuencias generales y metagenómicas, que incluyen TaraDB28, Metaclust22, MetaSourceDB29 y JGIclust30, usando HHblits y JackHMMER. Se generaron tres tipos de MSAs por DeepMSA2 (es decir, DeepMSA_qMSA, DeepMSA_dMSA y DeepMSA_mMSA) utilizando diferentes estrategias de búsqueda, resultando en alineamientos más profundos y diversos que son especialmente útiles para objetivos difíciles con pocas secuencias homólogas. 

En paralelo, MULTICOM utiliza DHR27 que aprovecha incrustaciones generadas por modelos de lenguaje de proteínas para buscar proteínas homólogas y generar MSAs adicionales. DHR es particularmente eficaz para mejorar la profundidad de alineamiento para objetivos con pocos homólogos cercanos, ayudando a aumentar la precisión predictiva para objetivos difíciles. 

Para enriquecer aún más las MSAs, empleamos ESM27 para generar dos secuencias sintéticas enmascarando sistemáticamente cada residuo en la secuencia de entrada, prediciendo sustituciones y seleccionando las sustituciones más confiables. Estas secuencias sintéticas se añadieron a la MSA Default_AF2, formando un alineamiento ampliado denominado ESM-MSA, que mejoró la diversidad y la generalización de las características de secuencia utilizadas en la predicción de estructuras. 

Finalmente, durante CASP16, la ColabfoldMSA proporcionada por CASP16 y el grupo Steinegger fue utilizada por MULTICOM4 para generar algunos modelos estructurales, algunos de los cuales fueron seleccionados como el sexto modelo enviado a CASP según lo solicitado. 

## Construcción de MSA basada en dominios 

Para objetivos multi-dominio, las MSAs de longitud completa pueden cubrir algunos dominios bien, pero tienen poca profundidad de secuencia para otros dominios, porque la búsqueda de secuencias de longitud completa podría estar dominada por algunos dominios grandes o dominios con muchas secuencias homólogas. Para abordar este problema, para objetivos de múltiples dominios, los límites de dominio se identifican utilizando un conjunto de herramientas de predicción de dominios (DomainParser31, UniDoc32, HHsearch33). Durante CASP16, también se probó la anotación manual de dominios. DomainParser y HHsearch se apoyan únicamente en la secuencia de proteínas, mientras que UniDoc y la inspección manual utilizan una estructura proteica prevista inicialmente para segmentar la proteína en dominios. Para aplicar HHsearch a la predicción de dominios para un objetivo, la MSA del objetivo es utilizada por HHsearch para construir un perfil representado como un modelo oculto de Markov (HMM). El perfil se busca contra una biblioteca de perfiles de plantilla interna (HMM) creada para las plantillas de proteínas en el PDB. La búsqueda suele identificar algunas plantillas alineadas con el objetivo. Las plantillas insignificantes con valor e (>1), longitud de secuencia (≤40 residuos) o cobertura de alineación (≤0.5) se filtrarán. Cada región continua del objetivo alineada con las plantillas restantes se trata como un dominio separado, y cualquier región no alineada mayor de 40 residuos también se considera un dominio. Además, DISOPRED334 se utiliza para predecir regiones desordenadas, que se incorpora para refinar y ajustar los límites de dominio para objetivos multi-dominio. 

Para cada dominio previsto, se generaron MSAs independientes utilizando el mismo procedimiento aplicado a las secuencias de longitud completa, incorporando diferentes fuentes de MSA como Default_AF2 y DeepMSA2_dMSA. Los alineamientos de dominios en sus MSAs se emparejaron en función de identificadores de secuencia compartidos. Para los alineamientos de dominio que no se pueden emparejar, se aplicó relleno de brechas a cada alineamiento de dominio para reconstruir un alineamiento de longitud completa. 

Communications Biology | (2025) 8:1587 

10 

Artículo 

https://doi.org/10.1038/s42003-025-08960-6 

**==> picture [451 x 601] intentionally omitted <==**

**----- Start of picture text -----**<br>
Bases de datos de secuencias de proteínas generales<br>Bases de datos metagenómicas<br>MSAs diversos pa<br>Segmentación de dominios<br>N<br>secuencia Dominio2secuencia Dominio3 secuencia<br>\.<br>J<br>MSA MSA de Dominio2 MSA de Dominio3 (<br>v<br>\. J<br>MSA P J N<br>Longitud total<br>MSA \- J<br>Alineación de alineación | Alineación de Domain3 N<br>Domain] Emparejado<br>Alineación de Domain] | Alineación de Domain2 | Alineación de<br>Domain3 er | er] \- J<br>a<br>Banco de Datos de Proteínas<br>PDB_sort90<br>ESMFold AiphaFolas 1 AlphaFold2 personalizado<br>1<br>1] MSA y Plantillas<br>Solo secuencia i A<br>&<br>1<br>1<br>1<br>1<br>1<br>1<br>—— 4<br>1 1 1 1 1<br>—)<br>@ Nodo (residuo)<br>— Arista (proximidad espacial o interacción)<br>**----- End of picture text -----**<br>


Fig. 10 | Visión general del módulo de predicción de estructura terciaria de MULTICOM4. El módulo comienza con el muestreo de alineación múltiple de secuencias (MSA) tanto en bases de datos generales de secuencias de proteínas (por ejemplo, UniRef30, UniRef90) como en fuentes metagenómicas especializadas (por ejemplo, BFD, MGnify) utilizando diferentes herramientas de alineación. Para objetivos multidominio, además de generar MSAs de longitud completa, se realiza la construcción de MSAs basados en dominios segmentando la secuencia objetivo en dominios, generando MSAs individuales de dominio y combinándolos en MSAs de longitud completa mediante el emparejamiento de alineaciones y el relleno de huecos. Las plantillas se identifican alineando 

perfiles de secuencia contra las bases de datos PDB70 y PDB_sort90. La predicción de la estructura se realiza utilizando múltiples predictores basados en aprendizaje profundo, incluyendo una canalización AlphaFold2 personalizada con varias MSAs y plantillas como entrada (principalmente), el servidor web AlphaFold3 (muestreo extensivo, principalmente) y ESMFold (solo para modelado de secuencias de proteínas individuales). Los modelos predichos se evalúan mediante múltiples métodos/métricas de evaluación de calidad de modelos (QA) (por ejemplo, GATE, PSS y plDDT) para seleccionar predicciones finales de alta confianza. 

Communications Biology | (2025) 8:1587 

11 

Artículo 

https://doi.org/10.1038/s42003-025-08960-6 

Cada MSA basado en dominio resultante se combina con dos MSAs de longitud completa (es decir, Default_AF2 o DeepMSA2_dMSA), respectivamente, para formar los MSAs basados en dominio finales. Por lo tanto, cada MSA basado en dominio consta de tres componentes: alineamientos de los MSAs de longitud completa, alineamientos de dominio pareados y alineamientos de dominio no pareados con relleno de huecos. Este procedimiento se repitió a través de múltiples combinaciones de métodos de predicción de dominio y fuentes de MSAs de longitud completa, dando como resultado 8 MSAs basados en dominio (cuatro estrategias de segmentación de dominio × dos fuentes de MSA). Estos MSAs basados en dominio se utilizaron en paralelo con los MSAs de longitud completa originales para mejorar la diversidad de alineamiento y aumentar la robustez de la predicción de estructura aguas abajo. 

## Identificación de plantillas 

Las plantillas se identifican alineando los perfiles de secuencia de un objetivo construido a partir del MSA generado en UniRef90 contra las bibliotecas de plantillas curadas de Protein Data Bank (PDB) usando HHsearch. Se emplean dos bibliotecas de plantillas: pdb70_v2024_03, una base de datos estándar incluida en AlphaFold2 que contiene modelos ocultos de cadenas HMM para un subconjunto representativo de cadenas PDB filtradas con una identidad de secuencia máxima del 70%; y PDB_sort9016, una base de datos interna curada filtrada al 90% de identidad de secuencia para mantener una mayor diversidad estructural. Utilizar ambas bibliotecas aumenta la probabilidad de identificar plantillas informativas estructuralmente, especialmente en regiones de baja homología, y mejora la calidad de las predicciones de plegamiento posteriores. 

## Generación de modelos 

Los modelos estructurales se generan usando tres predictores basados en aprendizaje profundo como sigue. Primero, AlphaFold2 se ejecuta en paralelo usando diferentes MSA, con o sin plantillas, y bajo configuraciones variables. Esto incluye cambiar el preset del modelo (monómero o monómero_ptm) y activar o desactivar el dropout en el Evoformer o en el módulo estructural. El número de predicciones de conjunto y pasos de reciclaje se fija en 1 y 8, respectivamente. Por cada objetivo, se generaron entre 2000 y 72,000 modelos usando AlphaFold2 durante CASP16. 

En segundo lugar, para explorar aún más el espacio de conformaciones, se utilizó el servidor web de AlphaFold3 de DeepMind para generar cientos a miles de modelos durante CASP16. Como el software de AlphaFold3 se lanzó después de que CASP16 concluyó, puede ser llamado por MULTICOM4 localmente para generar modelos estructurales. Para objetivos de etapa temprana, como T1207, donde AlphaFold3 aún no se había incorporado completamente al flujo, se generaron solo 10 modelos. Para otros objetivos, se generaron entre 200 y 5300 modelos utilizando AlphaFold3 durante CASP16. 

## Las estrategias de clasificación de modelos de los predictores MULTICOM en CASP16 

Durante CASP16, MULTICOM4 participó en la predicción de la estructura terciaria 

comocincopredictores que adoptan diferentes estrategias de clasificación de modelos. Estas incluyeron tres predictores de servidor: MULTICOM_AI, MULTICOM_GATE y MULTICOM_LLM, así como dos predictores humanos: MULTI-COM_human y MULTICOM. Aunque los cinco predictores compartían la misma canal de generación de modelos, difirieron en las estrategias de selección de los cinco mejores modelos para la entrega a CASP, que se describen a continuación. 

- MULTICOM_AI: Los modelos se clasificaron según las puntuaciones plDDT global. El modelo mejor clasificado se seleccionó junto con hasta cuatro modelos adicionales que fueran estructuralmente diversos, definidos por un TM-score menor de 0.8 entre ellos. Al menos un modelo generado por AlphaFold3 se incluyó si aún no estaba seleccionado. 

- MULTICOM_GATE: Los modelos se clasificaron usando las puntuaciones GATE. Se aplicó agrupamiento K-means para agrupar modelos estructuralmente similares y se seleccionó el modelo mejor clasificado de cada clúster. Se incluyó un modelo de AlphaFold3 si no ya estaba representado en la selecciónfinal. 

- MULTICOM_LLM: Inicialmente, los modelos se clasificaron en función del promedio de las puntuaciones GATE y plDDT global. Después de que los modelos AlphaFold3 se incorporaron al sistema durante las primeras etapas de CASP16, el modelo top-1 se seleccionó según la puntuación de clasificación de AlphaFold3, mientras que los otros cuatro modelos se eligieron usando el promedio de GATE y las puntuaciones plDDT global. 

- MULTICOM: Este predictor inicialmente utilizó puntuaciones globales de plDDT para la selección de modelos. Después de que se añadió AlphaFold3 al sistema, el modelo mejor clasificado se seleccionó en función del promedio de la puntuación de clasificación de AlphaFold3 y la puntuación GATE. Los modelos superiores restantes se seleccionaron utilizando métricas adicionales, incluido el promedio de GATE y las puntuaciones plDDT global, así como GATE, GCPNet-EMA, EnQA y PSS individualmente. Se aplicaron ajustes manuales cuando fue necesario para asegurar diversidad y calidad. 

- MULTICOM_human: La selección de modelos inicialmente se basó en las puntuaciones GATE. A medida que evolucionó la canal de predicción, se consideraron múltiples métricas de clasificación, incluido el promedio de global plDDT, GATE, GCPNet-EMA, EnQA y PSS. El modelo top-1 se seleccionó usando el promedio de GATE y las puntuaciones global plDDT, con supervisión humana aplicada según sea necesario. Después de que AlphaFold3 se integró por completo, la clasificación de modelos se basó principalmente en las puntuaciones global plDDT con refinamiento manual si fue necesario. 

## Estadísticas y reproducibilidad 

Finalmente, se utiliza ESMFold para generar un pequeño número de modelos alternativos, aumentando la diversidad estructural. A diferencia de AlphaFold2 y AlphaFold3, ESMFold solo desempeña un papel muy menor en la canal de predicción MULTICOM4, con solo 50 modelos generados para algunos objetivos durante CASP16. Todos los modelos producidos por AlphaFold2, AlphaFold3 y ESMFold se agrupan para la clasificación y selección de modelos. 

En la evaluación se utilizaron un total de 58 objetivos proteicos que comprenden 84 dominios. Las comparaciones estadísticas entre predictores se realizaron utilizando la prueba de Wilcoxon con rango firmado unilateral no paramétrica al 95% de nivel de confianza. 

## Resumen de informes 

## Selección de modelos 

La selección de modelos se basa en una combinación de las propias puntuaciones de confianza de AlphaFold y métodos de evaluación de calidad (QA) independientes. Internamente, cada predictor de estructura (p. ej., AlphaFold2, AlphaFold3, ESMFold) proporciona una puntuación lDDT global prevista o su equivalente para estimar la confianza de cada modelo estructural predicted. 

Dado que las puntuaciones de confianza autoestimadas no siempre pueden seleccionar buenos modelos estructurales, MULTICOM4 aplica varios métodos independientes de evaluación de calidad de modelo único o multi-modelo (basados en consenso) para clasificar la calidad de los modelos estructurales previstos. Dos métodos QA de modelo único, incluyendo EnQA y GCPNet-EMA, predicen la calidad de cada modelo individual utilizando enfoques de aprendizaje profundo. En cambio, tres métodos QA de múltiples modelos, como un método de transformador de grafos—GATE, DeepRank333 y la puntuación de similitud por pares promedio (PSS)—, consideran la similitud entre modelos en la evaluación de calidad del modelo. La clasificación final de modelos puede generarse combinando puntuaciones QA individuales de diferentes maneras. 

Más información sobre el diseño de la investigación está disponible en el Resumen de Informes de la Nature Portfolio vinculado a este artículo. 

## Disponibilidad de datos 

Las estructuras de proteínas de los objetivos monómeros de CASP16 están disponibles en https://predictioncenter.org/download_area/CASP16/targets/. Los modelos estructurales de proteínas y los datos analíticos generados en este estudio están disponibles en 

https://zenodo.org/records/1558816235.Datos de fuente para las figuras son proporcionados en Datos Suplementarios 1. Todos los demás datos están disponibles del autor correspondiente a petición razonable. 

## Disponibilidad de código 

El código fuente de MULTICOM4 está disponible https://github.com/ en: BioinfoMachineLearning/MULTICOM436. 

Recibido: 7 de junio de 2025; Aceptado: 26 de septiembre de 2025; 

**==> picture [133 x 12] intentionally omitted <==**

Communications Biology | (2025) 8:1587 

12 

Artículo 

https://doi.org/10.1038/s42003-025-08960-6 

## Referencias 

1. Eickholt, J. & Cheng, J. Predicción de contactos residuo-residuo de proteínas utilizando redes profundas y boosting. Bioinformatics 28, 3066–3072 (2012). 

2. Hou, J., Adhikari, B. & Cheng, J. Deepsf: red neuronal convolucional profunda para mapear secuencias de proteínas a pliegues. Bioinformatics 34, 1295–1303 (2018). 

3. Adhikari, B., Hou, J. & Cheng, J. Dncon2: predicción mejorada de contactos de proteínas usando redes neuronales convolucionales profundas de dos niveles. Bioinformatics 34, 1466–1472 (2018). 

4. Xu, J. Plegamiento de proteínas basado en distancias potenciado por aprendizaje profundo. Proc. Natl Acad. Sci. 116, 16856–16865 (2019). 

5. Senior, A. W. et al. Predicción mejorada de la estructura de proteínas usando potenciales de aprendizaje profundo. Nature 577, 706–710 (2020). 

6. Baek, M. et al. Predicción precisa de estructuras y interacciones de proteínas usando una red neuronal de tres vías. Science373, 871–876 (2021). 

7. Lin, Z. et al. Predicción a escala evolutiva de la estructura de proteínas a nivel atómico la estructura de proteínas con un modelo de lenguaje. Science 379, 1123–1130 (2023). 

8. Jumper, J. et al. Predicción altamente precisa de la estructura de proteínas con alphafold. Nature 596, 583–589 (2021). 

9. Vaswani, A. et al. Attention is all you need. In Advances in Neural Sistemas de Procesamiento de Información 30 (Curran Associates, Inc., 2017). 

   26. Zheng, W. et al. Mejorando el aprendizaje profundo para la predicción de monómeros y predicción de estructuras complejas usando deepmsa2 con grandes datos metagenómicos. Nat. Methods 21, 279–289 (2024). 

   27. Hong, L. et al. Detección rápida y sensible de homólogos de proteínas usando recuperación densa profunda. Nat. Biotechnol. 43, 983–995 (2025). 

   28. Wang, Y. et al. Impulsando el plegamiento ab initio con metagenómica marina permite la predicción de estructura y función de nuevas familias de proteínas. Genome Biol. 20,1–14 (2019). 

   29. Yang, P., Zheng, W., Ning, K. & Zhang, Y. Descifrando la relación de nichos del microbioma con secuencias homólogas permite una predicción precisa de la estructura de proteínas. Proc. Natl Acad. Sci. 118, e2110828118 (2021). 

   30. Nordberg, H. et al. El portal del genoma del departamento de energía joint genome institute: actualizaciones 2014. Nucleic Acids Res.42, D26–D31 (2014). 

   31. Xu, Y., Xu, D. & Gabow, H. N. Descomposición de dominios de proteínas usando un enfoque basado en teoría de grafos. Bioinformatics 16, 1091–1104 (2000). 

   32. Zhu, K., Su, H., Peng, Z. & Yang, J. Un enfoque unificado para el análisis de dominios con una matriz de distancias entre residuos. Bioinformatics 39, btad070 (2023). 

   33. Liu, J., Wu, T., Guo, Z., Hou, J. & Cheng, J. Mejorando la estructura terciaria de proteínas predicción de estructuras por aprendizaje profundo y predicción de distancias en casp14. Proteins Struct. Funct. Bioinform. 90,58–72 (2022). 

10. Lensink, M. F. et al. Predicción de ensamblajes de proteínas, la próxima frontera: 34. Jones, D. T. & Cozzetto, D. Disopred3: región desordenada precisa el experimento casp14-capri. Proteins Struct. Funct. Bioinform. predicciones con actividad de unión a proteínas anotada. 89, 1800–1823 (2021). Bioinformatics 31, 857–863 (2015). 

11. Evans, R. et al. Predicción de complejos proteicos con alphafold-multimer. Preprint en bioRxiv https://www.biorxiv.org/content/10.1101/2021.10.04.463034v22021–10 (2021). 

   35. Liu, J., Neupane, P. & Cheng, J. Potenciando la estructura terciaria de proteínas con alphafold predicción de estructuras mediante ingeniería msa602 y muestreo y clasificación extensos de modelos en casp16. https://doi.org/10.5281/603zenodo.15588162.604 (2025). 

12. Abramson, J. et al. Predicción precisa de la estructura de biomoléculas interacciones con AlphaFold 3. Nature 630, 493–500 (2024). 

   36. Liu, J. & Cheng, J. Bioinfomachinelearning/multicom4: Multicom4 https://doi.org/10.5281/zenodo.17102713 (2025). 

13. Ho, J., Jain, A. & Abbeel, P. Modelos probabilísticos de difusión con denoising. Adv. Neural Inf. Process. Syst. 33, 6840–6851 (2020). 

## Agradecimientos 

14. Liu, J., Neupane, P. & Cheng, J. Mejorando Alphafold2 y 3-basado predicción de la estructura de complejos proteicos con multicom4 en casp16. Proteins 2025 (2025). 

Agradecemos a los organizadores y evaluadores de CASP16 por hacer disponibles los datos de CASP16. Este trabajo está parcialmente financiado por dos subvenciones NIH [R01GM093123 y R01GM146340]. 

15. Eswar, N., Eramian, D., Webb, B., Shen, M.-Y. & Sali, A. Proteína modelado de estructuras con modeller. en Structural Proteomics: High-throughput Methods 145–159 (Humana Press, 2008). 

## Contribuciones de los autores 

J.C. concibió el proyecto. J.C., J.L. y P.N. diseñaron el experimento. J.L., P.N. y J.C. realizaron el experimento y recopilaron los datos. J.L., J.C. y P.N. analizaron los datos. J.L., J.C. y P.N. redactaron el manuscrito. 

16. Liu, J. et al. Mejorando la estructura terciaria de proteínas basada en alphafold2 predicción con multicom en casp15. Commun. Chem. 6, 188 (2023). 

17. Liu, J., Neupane, P. & Cheng, J. Estimación del modelo de complejo proteico exactitud utilizando transformers de grafos y grafos de similitud por pares. Bioinform. Adv. 5, vbaf180 (2025). 

## Intereses competentes 

Los autores declaran no tener intereses en competencia. 

18. Liu, J. et al. Mejorando el complejo proteico basado en alphafold-multimer predicción de estructuras con multicom en casp15. Commun. Biol. 6, 1140 (2023). 

## Información adicional 

Información suplementaria La versión en línea contiene material suplementario disponible en https://doi.org/10.1038/s42003-025-08960-6. 

19. Mirdita, M. et al. Bases de datos Uniclust de agrupados y profundamente secuencias de proteínas anotadas y alineaciones. Nucleic Acids Res. 45, D170–D176 (2017). 

20. Consortium, U. Uniprot: un centro mundial de conocimiento de proteínas. Nucleic Acids Res. 47, D506–D515 (2019). 

Correspondencia y solicitudes de materiales deben dirigirse a Jianlin Cheng. 

21. Steinegger, M., Mirdita, M. & Söding, J. Ensamblaje a nivel de proteína aumenta la recuperación de secuencias de proteínas de muestras metagenómicas en varios órdenes. 

La información de revisión por pares Communications Biology agradece a R. Dustin Schaeffer y a los otros revisores anónimos por su contribución al proceso de revisión. Editores de manejo primario: Luciano Abriata y Laura Rodríguez Pérez. Un archivo de revisión por pares está disponible. 

22. Steinegger, M. & Söding, J. Agrupación de enormes conjuntos de secuencias de proteínas en tiempo lineal. Nat. Commun. 9, 2542 (2018). 

23. Mitchell, A. L. et al. Mgnify: el recurso de análisis del microbioma en 2020. Nucleic Acids Res. 48, D570–D578 (2020). 

La información sobre reimpresiones y permisos está disponible en http://www.nature.com/reprints 

24. Remmert, M., Biegert, A., Hauser, A. & Söding, J. Hhblits: relámpagobúsqueda rápida e iterativa de secuencias de proteínas por alineamiento hmm-hmm. Nat. Methods 9, 173–175 (2012). 

25. Johnson, L. S., Eddy, S. R. & Portugaly, E. Modelo oculto de Markov procedimiento heurístico rápido y de búsqueda HMM iterativa. BMCBioinform. 11,1–8 (2010). 

Nota del editor. Springer Nature continúa neutral respecto a reclamaciones de jurisdicción en mapas publicados e afiliaciones institucionales. 

Communications Biology | (2025) 8:1587. 

13 

Artículo 

https://doi.org/10.1038/s42003-025-08960-6 

Acceso abierto Este artículo está licenciado bajo una Licencia de Atribución 4.0 Internacional de Creative Commons, que permite el uso, compartir, adaptar, distribuir y reproducir en cualquier medio o formato, siempre que se otorgue el crédito adecuado al autor o autores originales y a la fuente, se proporcione un enlace a la licencia de Creative Commons e indique si se realizaron cambios. Las imágenes u otro material de terceros en este artículo están incluidos bajo la licencia de Creative Commons del artículo, a menos que se indique lo contrario en una línea de crédito del material. Si el material no está incluido en la licencia de Creative Commons del artículo y su uso previsto no está permitido por la regulación estatutaria o excede el uso permitido, deberá obtener permiso directamente del titular de los derechos de autor. Para ver una copia de esta licencia, visite http://creativecommons.org/licenses/by/4.0/. 

- © Los/las Autor(es) 2025 

Communications Biology | (2025) 8:1587 

14 

