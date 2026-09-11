# Documento de revisión adversarial — MVA Hackathon 2026, Track 2

**Para:** un revisor externo (humano o IA) y el equipo médico del caso.
**Equipo:** `checkpoint-in-trans` · **Probando:** `PROBAND01` (muestra `WGS_EX2312012`)
**Repositorio:** https://github.com/tlondonoz/RarekidMVA
**Fecha de la revisión solicitada:** tras el cierre del paquete de entrega del Track 2.

---

## 0. Instrucciones para quien revisa

Tu tarea **no** es mejorar la redacción ni confirmar que el trabajo parece sólido. Es **intentar
romperlo**. Concretamente:

1. **Busca sobreafirmaciones.** Cada vez que el documento diga que algo está "descartado",
   "confirmado" o "demostrado", comprueba si la evidencia citada sostiene ese verbo o solo uno más
   débil. La distinción entre *no evaluado* y *negativo* es la que más nos importa vigilar.
2. **Comprueba las cifras** contra la sección 7, que lista cada número con el fichero del que sale.
   Todas proceden de artefactos guardados, no de memoria. Si alguna no cuadra, es un fallo real.
3. **Ataca la cadena causal de cada candidato**, no el candidato. La pregunta no es "¿es dasatinib
   un fármaco razonable?" sino "¿el salto desde *este* genotipo hasta *esa* diana aguanta?".
4. **Busca lo que falta.** Ejes terapéuticos que no consideramos, bases de datos que no consultamos,
   mecanismos alternativos compatibles con el mismo genotipo.
5. **Señala dónde el sesgo de publicación nos habrá engañado.** Gran parte de la evidencia viene de
   extracción estructurada sobre resúmenes de PubMed, que sobre-representa resultados positivos.

Los entregables que auditas están **en inglés**; este documento está en español para el equipo
médico. Las afirmaciones críticas se citan literalmente en inglés.

**Aviso de datos:** el caso procede de una copia desidentificada del repositorio del reto. Este
documento contiene dos coordenadas genómicas que ya son públicas en la submission y en el
repositorio. No contiene identificadores del paciente. Aun así, si tu organización tiene una política
sobre datos genómicos, aplícala antes de pegarlo en un servicio que retenga entradas.

---

## 1. El caso, en una página

Niño con **aneuploidía variegada en mosaico (MVA)** y rabdomiosarcoma. Secuenciación de genoma
completo Illumina sobre sangre periférica.

**Track 1 (ya evaluado y puntuado):** par heterocigoto compuesto en *BUB1B*.

| | Alelo 1 | Alelo 2 |
|---|---|---|
| GRCh38 | chr15:40209701 T>G | chr15:40220612 T>G |
| HGVS (ENST00000287598.11, MANE Select) | c.2210T>G, p.Leu737Ter | c.3006T>G, p.Asn1002Lys |
| Consecuencia | codón de parada prematuro | missense en el dominio pseudoquinasa |
| Clasificación ACMG propia | Patogénica | VUS |

**Resultado externo:** el evaluador del reto devolvió *Full match* en el primer puesto, F-max 1.000.
Coincidieron **las dos** variantes. Es decir, el segundo alelo que clasificamos como VUS por no poder
demostrar la fase es el correcto.

**Cómo debe leerse eso, y es importante para la revisión:** no valida aplicar el criterio PM3 sin
fase. La clasificación VUS era la correcta con la evidencia disponible. Lo que valida es el
razonamiento mecanístico que llevó a proponer el par. Si en la revisión encuentras que usamos el
resultado del leaderboard como respaldo de una decisión metodológica, eso es un fallo y queremos
saberlo.

**La fase sigue sin demostrarse.** Las dos variantes están a 10,911 pb, el llamador no las asignó a
ningún grupo de fase física, y con lecturas cortas no es resoluble. Haría falta muestra parental o
lecturas largas.

---

## 2. Track 2 — la tesis en tres frases

1. La lesión es **insuficiencia de dosis de un módulo de andamiaje**, no una ganancia de función.
2. Por tanto **no hay nada que inhibir**, y lo verificamos en lugar de asumirlo.
3. Los candidatos actúan sobre las **consecuencias** (senescencia, mTORC1) o intentan **restaurar la
   proteína** (lectura a través), y ese tercer eje quedó degradado por nuestro propio análisis.

---

## 3. Caracterización del mecanismo, con su evidencia

### 3.1 BubR1 es pseudoquinasa en vertebrados

De los resúmenes recuperados que se pronuncian sobre la actividad catalítica del dominio C-terminal,
**13 de 16 concluyen que la proteína de vertebrados es catalíticamente inactiva**.

Los tres discrepantes, examinados uno a uno:

| PMID | Organismo | Qué mide realmente |
|---|---|---|
| 17702574 | *Drosophila* | Alelo mutante en el dominio quinasa que retiene actividad del SAC mitótico |
| 31201382 | *Drosophila melanogaster* | Estructura del dominio quinasa con plegamiento catalíticamente competente — quinasa genuina |
| 24431077 | **humano** | **No mide catálisis.** Infiere "actividad quinasa" de que la unión de sinucleína-γ compromete la función del checkpoint — lectura que el modelo de andamiaje explica igual de bien |

*Este desglose corrige una versión previa que atribuía los tres discrepantes a* Drosophila. *Se
señala aquí porque un revisor que mire el historial del repositorio verá el commit de corrección.*

El dominio sigue siendo **esencial como andamio**: requerido para promover la fosforilación de KARD y
el reclutamiento al cinetocoro (PMID 33207204), y para mantener el balance quinasa-fosfatasa en el
cinetocoro externo (PMID 33860079).

**Consecuencia operativa:** `p.Asn1002Lys` es una lesión estructural, no catalítica. Un inhibidor
competitivo de ATP contra BubR1 habría sido conceptualmente incorrecto.

**Discrepancia con base de datos, declarada:** UniProt O60566 todavía anota `EC 2.7.11.1` y un sitio
activo en Asp882. Nos apartamos de la anotación y nos quedamos con la literatura primaria. Si
consideras que eso es un error, dilo.

### 3.2 Qué hace cada alelo

**`p.Leu737Ter`** elimina el dominio pseudoquinasa completo (766–1050). Se conserva todo lo
N-terminal: dominio N-terminal de BUB1 (62–226), región de interacción con KNL1 (152–185), señal de
localización nuclear y caja D. El stop está **314 codones** antes del stop natural,
así que el transcrito es competente para degradación mediada por codón sin sentido.

**`p.Asn1002Lys`** desestabiliza ese mismo dominio desde dentro:

- Accesibilidad relativa al disolvente: **20.1 %** — parcialmente enterrado.
- Confianza local del modelo: pLDDT **91.1**, frente a 81.9 de media del dominio.
- Empaquetado contra un grupo aromático: LEU1001, ALA1003, TRP978, VAL998, ASN1004, ILE1000 entre otros.
- Distancia al aspartato catalítico degenerado: **19.8 Å**.
- Distancia a la lisina de unión a nucleótido: **34.7 Å** — no es residuo de bolsillo.

**Limitación estructural grave, declarada:** **ninguna estructura experimental cubre el residuo
1002**. Las dos estructuras crio-EM del complejo APC/C–MCC cuyo rango de alineamiento parecía
cubrirlo (6TLJ, 5KHU) resuelven **0 de los 285 residuos** del dominio pseudoquinasa. Todo el análisis
estructural descansa en el modelo de AlphaFold. Esto es atacable y queremos que se ataque.

### 3.3 El modelo animal más cercano

**PMID 31738183** construyó ratones `BubR1^L1002P` que imitan la variante humana `BUBR1^L1012P` (la
numeración de ratón va 10 residuos por detrás) y los cruzó con un alelo hipomórfico de baja proteína.
`BubR1^H/L1002P` es **viable** y muestra el fenotipo MVA completo: predisposición a cáncer, vida
corta, enanismo, lipodistrofia, sarcopenia y baja tolerancia al estrés cardíaco.

Eso es **proteína reducida + missense en el lóbulo C**, la misma arquitectura alélica que
`p.Leu737Ter` + `p.Asn1002Lys`.

**Calibración que hicimos explícita para no sobrevender la analogía:** el residuo humano 1012 es
leucina y está completamente enterrado (0 % de accesibilidad, pLDDT 95.3), pero está a **10.3 Å** de
Asn1002 y **no comparten ningún contacto**. La analogía es de **arquitectura alélica**, no de
microentorno estructural. Si crees que aun así la presentamos con demasiado peso, dilo.

Dos nodos mecanísticos salen de ese trabajo, y son el origen de los candidatos 1 y 2:
- La severidad progeroide **sigue a la complejidad del fenotipo secretor de senescencia** en músculo esquelético.
- La predisposición a sarcopenia **correlaciona con hiperactividad de mTORC1**.

---

## 4. Por qué no hay diana directa (y por qué no hicimos docking)

Open Targets evalúa **28 categorías de tratabilidad** para *BUB1B*. Cinco positivas,
ninguna usable:

- `SM:High-Quality Ligand`
- `SM:Druggable Family`
- `PR:Literature`
- `PR:UniProt Ubiquitination`
- `PR:Database Ubiquitination`

Leído por modalidad:

- **Molécula pequeña:** sin fármaco aprobado, sin compuesto en fase clínica, sin estructura con
  ligando y — decisivo — **sin bolsillo de calidad alta ni de calidad media**. Las dos positivas son
  "ligando de calidad" y "familia druggable"; esta última es un artefacto de estar anotado como
  quinasa, justo lo que la sección 3.1 desmiente.
- **Anticuerpo:** todas negativas (diana intracelular).
- **Degradación dirigida:** tres positivas — pero degradar es lo contrario de lo que necesita una
  insuficiencia de dosis.

**Decisión metodológica que más nos interesa que revises:** el usuario pidió explícitamente docking.
Argumentamos que no procedía, por tres razones acumulativas: (a) no hay bolsillo donde acoplar;
(b) la dirección terapéutica es restaurar, no inhibir, y el docking presupone unir algo a la proteína
que hace falta aumentar; (c) los tres candidatos actúan sobre dianas cuyas afinidades
fármaco-diana ya están medidas experimentalmente, de modo que un docking re-derivaría peor algo ya
medido.

**Contraargumento que un revisor podría hacer, y que no hemos refutado:** el docking podría haberse
usado no sobre BubR1 sino sobre la interfaz BubR1–CDC20 o BubR1–BUB3, buscando un estabilizador de
interacción proteína-proteína (un "molecular glue") que aumente la función del complejo residual.
No exploramos esa vía. Si te parece que es un hueco, es probablemente **el hueco más serio del
trabajo**.

---

## 5. Los candidatos, con su cadena y sus objeciones

### Candidato 1 — Dasatinib (± quercetina), senolítico

**Cadena:** insuficiencia de BubR1 → senescencia celular en múltiples tejidos (endotelio y barrera
hematoencefálica PMID 26883501; músculo esquelético PMID 26464273; corazón PMID 40607964;
progenitores neurales PMID 28383136; fibroblastos haploinsuficientes PMID 26847209) → en el ratón de
arquitectura equivalente, la severidad progeroide sigue a la complejidad del fenotipo secretor
(PMID 31738183) → la eliminación farmacológica de células senescentes mejora el fenotipo
(PMID 42098153 en modelo hipomórfico; PMID 41564845 función renal, p16, fibrosis) → existen datos en
humanos (PMID 39823170, PMID 39510246).

**Encaje regulatorio, el más fuerte del conjunto:** `DASATINIB` devuelve **12
solicitudes** en Drugs@FDA con estado `Prescription`, y la ficha técnica incluye
indicación pediátrica **desde 1 año de edad**, una de ellas *"in combination with chemotherapy"*.
Dosificación, farmacocinética y seguridad en un niño bajo quimioterapia concurrente ya están
caracterizadas — que es exactamente la situación del paciente.

**Objeciones que nosotros mismos ponemos:**
- La quercetina **no es un fármaco FDA** (0 solicitudes). El par clásico D+Q
  no son dos medicamentos aprobados.
- Ningún ensayo senolítico en MVA ni en niños para esta indicación.
- Mielosupresión y derrame pleural, que se suman a la toxicidad de la quimioterapia.
- **La objeción mayor:** la senescencia es un programa **tumor-supresor**. Eliminarla en un niño con
  síndrome de predisposición a cáncer y un rabdomiosarcoma activo no es maniobra inocua. Es el punto
  que más nos preocupa y el que más querríamos ver atacado.

### Candidato 2 — Sirolimus o everolimus, inhibición de mTORC1

**Cadena:** hiperactividad de mTORC1 en ratones mutantes de BubR1 (PMID 31738183) → la inhibición de
mTOR pospone el envejecimiento prematuro en modelos progeroides independientes (PMID 32282093
prelamina A; PMID 31312666 rapamicina rescata defectos de diferenciación en Zmpste24−/−;
PMID 29581305 everolimus aumenta autofagia en laminopatías). Ambos aprobados con uso pediátrico.

**Objeciones propias:**
- **La relación BubR1–mTOR no es direccionalmente consistente:** en hepatocarcinoma, BUB1B alto
  *sube* mTORC1 (PMID 32977361), lo contrario del hallazgo progeroide.
- **No recuperamos ningún experimento de rapamicina o everolimus en un modelo de BubR1.** El paso
  farmacológico es una inferencia cruzada entre síndromes progeroides, no un resultado directo.
- Inmunosupresión en un niño bajo quimioterapia citotóxica.

### Candidato 3 — Lectura a través, y el análisis que lo degradó

**A favor, el contexto del codón.** `c.2210T>G` convierte el codón `TTA` de Leu737 en
**`TGA`**, con `A` en la posición +4 → tetranucleótido **`TGAA`**.
Contexto: `CCAGAG[TGA]AGTGCC`. TGA es la clase de parada más permisiva a la lectura a través, y el contexto
exacto está caracterizado: TCP-306 es potente contra TGA-A mientras G418 prefiere TGA-C
(PMID 41730613); otros compuestos son particularmente eficaces en UGAA (PMID 42034525).
**Una recomendación de clase se detendría aquí y concluiría que el eje es prometedor.**

**En contra, el producto.** La lectura a través no restaura leucina: en UGA inserta
**W, C, R**. Preguntamos si BubR1 tolera alguno en la posición 737, leyendo el
residuo alineado a la posición humana 737 en **247 ortólogos de vertebrados**:

| Residuo en la posición 737 | Ortólogos |
|---|---|
| L | 236 |
| S | 5 |
| F | 2 |
| hueco de alineamiento | 2 |
| I | 1 |
| P | 1 |

**Ninguno de W, C, R aparece en ninguna especie** ({'W': 0, 'C': 0, 'R': 0}). La posición
está **10.2 %** accesible —es decir, ~90 % enterrada— y contacta con
PRO802, PHE805, TYR806, LEU809, residuos
del propio dominio pseudoquinasa.

Coste fisicoquímico en un sitio enterrado: Leu→Trp **+61.1 Å³**; Leu→Cys **−58.2 Å³** (deja cavidad);
Leu→Arg **−8.3** unidades de hidrofobicidad Kyte–Doolittle (entierra carga positiva).

**Y el sustrato escasea:** el codón de parada prematuro está 314 codones antes del
natural, competente para degradación, y la degradación del transcrito limita documentadamente la
eficacia de la lectura a través (PMID 34828417).

**Y el estado regulatorio remata.** `ATALUREN` devuelve **0 solicitudes** en
Drugs@FDA — nunca aprobado en EE. UU. — y la Comisión Europea **no renovó** su autorización
condicional el **28 de marzo de 2025**, tras concluir el CHMP que la eficacia no pudo confirmarse; la
ficha de la EMA figura como expirada. Sigue disponible en Reino Unido y los países de la UE pueden
acogerse a los artículos 117(3) y 5(1) de la Directiva 2001/83. Los aminoglucósidos son antibióticos
aprobados pero oto- y nefrotóxicos en administración crónica.

**Conclusión del eje, calibrada:** no está muerto — la alternativa a una proteína completa
desestabilizada es *no tener proteína*, y la enfermedad depende de dosis. Pero baja de "restaura
proteína casi silvestre" a "produce proteína completa de estabilidad incierta, sin medicamento
aprobado disponible".

### Contraindicación — letalidad sintética dirigida al SAC

Las células tumorales aneuploides dependen más del checkpoint residual y son selectivamente sensibles
a su perturbación (PMID 33505028, 33505027). Esa es la base estándar de los inhibidores de TTK/MPS1,
AURKA y CENP-E en tumores aneuploides, y una lectura ingenua la aplicaría al rabdomiosarcoma de este
niño.

**No debe aplicarse aquí.** Esa ventana terapéutica existe porque las células normales conservan un
checkpoint intacto mientras las tumorales no. En una insuficiencia constitucional de *BUB1B*, **el
tejido normal del paciente también tiene el checkpoint comprometido**, de modo que la ventana puede
ser estrecha, inexistente o invertida.

**A nivel de hipótesis, sin evidencia:** la dexametasona regula a la baja genes de G2/M y del
checkpoint del huso y permite a las células saltárselo (PMID 33478100). La dexametasona es de uso
corriente en oncología pediátrica. Si eso interacciona con un defecto constitucional del checkpoint
es desconocido y no está estudiado. Lo marcamos como pregunta, no como hallazgo.

**Sobre venenos del huso en general, la evidencia no sostiene nada:** de los resúmenes que reportan
dirección para células con checkpoint debilitado, **30 dicen más sensible y 18 más resistente**. La
literatura está genuinamente dividida. **Nada justifica alterar la quimioterapia del niño.**

---

## 6. La aportación metodológica, y su alcance

El paso que cambió nuestro propio orden —preguntar qué aminoácido instala realmente el fármaco y si
la proteína lo tolera— no es específico de este niño. Aplica a **cualquier enfermedad recesiva con un
alelo sin sentido**.

`code/ptc_triage.py` lo implementa. Entrada: transcrito y variante. Salida: identidad y clase de
permisividad del codón de parada, nucleótido +4 y tetranucleótido, competencia para degradación por
distancia al stop natural, residuos near-cognate insertables, distribución de residuos en esa
posición entre ortólogos de vertebrados, y listas explícitas de factores favorables y desfavorables.

```
$ python ptc_triage.py --refseq NM_001211.6 --cds-pos 2210 --alt G --uniprot O60566
  stop_codon: TGA    tetranucleotide: TGAA    permissiveness: most permissive
  near_cognate_products: ['W', 'C', 'R']    orthologs_aligned: 247
  products_seen_in_orthologs: {'W': 0, 'C': 0, 'R': 0}
  favourable:   stop codon TGA is the most permissive class
  unfavourable: PTC is NMD-competent, so transcript availability limits yield
                none of ['W','C','R'] occurs at this position in 247 orthologs
```

**Límites de la herramienta, declarados:** el conjunto de residuos near-cognate está codificado desde
la literatura general y **no se mide para el contexto de secuencia concreto**; las frecuencias
relativas de inserción en este sitio son desconocidas. La tolerancia por ortólogos es un argumento
**evolutivo, no un ensayo funcional**: la ausencia de un residuo en 247 vertebrados es evidencia
fuerte de constricción, no prueba de que la sustitución abole la función.

---

## 7. Tabla de verificación — cada cifra y su origen

Todas las cifras se leyeron de artefactos guardados en el momento de redactar. Fichero de respaldo:
`t2/review_values.json`.

| Afirmación | Valor | Fichero de origen |
|---|---|---|
| Abstracts que se pronuncian sobre catálisis | 13 inactiva / 3 activa (de 16) | `t2/lit_bubr1_kinase.tsv` |
| Abstracts extraídos en total (5 ejes) | 423 | `t2/lit_*.tsv` (bubr1_kinase=35, mtor=55, readthrough=98, senolytic=158, spindle=77) |
| Accesibilidad de Asn1002 | 20.1 % | `t2/residue1002_af.json` |
| pLDDT de Asn1002 / media del dominio | 91.1 / 81.9 | `t2/residue1002_af.json`, `t2/residue737_af.json` |
| Distancia 1002 → sitio de nucleótido | 34.7 Å | `t2/residue1002_af.json` |
| Distancia 1002 → aspartato catalítico | 19.8 Å | `t2/residue1002_af.json` |
| Accesibilidad de Leu737 | 10.2 % | `t2/residue737_af.json` |
| Codón silvestre → mutado | TTA → TGA | `t2/ptc_triage_BUB1B.json` |
| Tetranucleótido de terminación | TGAA | `t2/ptc_triage_BUB1B.json` |
| Codones hasta el stop natural | 314 | `t2/ptc_triage_BUB1B.json` |
| Ortólogos alineados | 247 | `t2/ortholog_positions.tsv` |
| Leu en la posición 737 | 236 | `t2/ortholog_positions.tsv` |
| Trp / Cys / Arg en la posición 737 | 0 / 0 / 0 | `t2/ortholog_positions.tsv` |
| Asn en la posición 1002 | 226 | `t2/ortholog_positions.tsv` |
| Lys en la posición 1002 | 0 | `t2/ortholog_positions.tsv` |
| Categorías de tratabilidad / positivas | 28 / 5 | `handoff/bub1b_tractability.json` |
| Solicitudes FDA de dasatinib | 12 (Prescription) | `handoff/fda_status.json` |
| Solicitudes FDA de ataluren | 0 | `handoff/fda_status.json` |
| Solicitudes FDA de quercetina | 0 | `handoff/fda_status.json` |
| Venenos del huso: sensible / resistente | 30 / 18 | `t2/lit_spindle.tsv` |

**Inconsistencia conocida, declarada aquí para que no la descubras como fallo:** la conservación de
la posición 737 se reporta como **95.5 %** en el informe (236 de 247,
incluyendo los 2 huecos de alineamiento en el denominador) y como
**96.3 %** en la salida de `ptc_triage.py` (236 de
245, excluyendo huecos). Son el mismo dato con distinto denominador. El informe
usa el conservador. No lo hemos unificado.

---

## 8. Limitaciones, completas

1. **Ningún candidato tiene evidencia clínica en MVA.** Ninguno se ha ensayado en esta enfermedad, en
   este gen, ni en este grupo de edad para esta indicación. Todos son hipótesis para seguimiento.
2. **La justificación senolítica descansa en genética de ratón**, y el paso farmacológico se apoya en
   un estudio recuperado en modelo hipomórfico, no en un ensayo.
3. **La justificación de mTORC1 es correlativa** en BubR1 y direccionalmente inconsistente entre
   contextos.
4. **Ninguna estructura experimental cubre ninguna de las dos posiciones.** Todo el análisis
   estructural sale del modelo de AlphaFold, con confianza local alta pero sin validación
   experimental.
5. **Los residuos near-cognate se toman de la literatura general**, no medidos para este contexto.
6. **La tolerancia por ortólogos es evidencia evolutiva, no un ensayo funcional.**
7. **No se hizo docking ni co-plegado.** La sección 4 da la razón, y también el contraargumento que
   no hemos refutado (interfaz proteína-proteína).
8. **No se modeló el riesgo oncológico.** La interacción entre terapia senolítica y un síndrome de
   predisposición a cáncer activo es la mayor pregunta abierta y queda fuera de lo que este análisis
   resuelve.
9. **Sesgo de recuperación.** La evidencia procede de extracción estructurada sobre resúmenes de
   PubMed mediante consultas que nosotros diseñamos. Ejes que no se nos ocurrieron no aparecen.
10. **Sin GPU ni cómputo remoto** (8 núcleos, ~3 GiB de RAM). No es la razón de ninguna decisión
    metodológica del Track 2, pero sí bloqueó en el Track 1 la detección de inserciones de elementos
    móviles en intrones de *BUB1B*, que quedó **sin evaluar, no descartada**.
11. **La fase de las dos variantes sigue sin demostrarse.**

---

## 9. Preguntas concretas para quien revisa

1. ¿El salto desde "insuficiencia de BubR1 causa senescencia en ratón" hasta "dasatinib en este niño"
   aguanta, o hay un eslabón que estamos dando por bueno?
2. ¿Cómo pesarías el riesgo de eliminar células senescentes en un síndrome de predisposición a
   cáncer con tumor activo? ¿Es descalificante o manejable con diseño?
3. **La interfaz proteína-proteína como diana** (estabilizar BubR1–CDC20 o BubR1–BUB3 en lugar de
   inhibir): ¿es una vía real que deberíamos haber explorado?
4. ¿Hay ejes terapéuticos que no consideramos? Pensamos en senolíticos, mTORC1 y lectura a través.
   ¿Y chaperonas farmacológicas para estabilizar el producto missense? ¿Inhibición de la degradación
   mediada por codón sin sentido combinada con lectura a través? ¿Modulación del punto de control por
   otra vía?
5. ¿La contraindicación sobre letalidad sintética dirigida al SAC está bien razonada, o estamos
   siendo excesivamente cautos con una estrategia que podría tener ventana suficiente?
6. ¿Alguna cifra de la sección 7 no cuadra con su fichero de origen?
7. ¿Hay algún sitio donde digamos "descartado" cuando la evidencia solo permite "no evaluado"?

---

## 10. Qué pondría a prueba cada hipótesis

| Experimento | Qué candidato prueba |
|---|---|
| Marcadores de senescencia (p16^INK4a, SA-β-gal, panel de fenotipo secretor) en fibroblastos del paciente | Si la carga senescente que justifica el candidato 1 está presente en este niño |
| Dasatinib ± quercetina *ex vivo* sobre esos fibroblastos, midiendo eliminación de células senescentes | El candidato 1, directamente, sin exponer al paciente |
| Fosfo-S6 y fosfo-4E-BP1 en fibroblastos del paciente | Si mTORC1 está hiperactivo en este genotipo, como asume el candidato 2 |
| Western de BubR1 completo ± agente de lectura a través en células del paciente | El candidato 3 — si se recupera algo de proteína completa |
| Ensayo de reto con colcemid sobre el checkpoint del huso (PMID 10877982), antes y después | La lectura funcional común a los tres |

La última fila es la que más importa: los tres candidatos se juzgan en última instancia por si mejora
la función del checkpoint o sus consecuencias, y ese ensayo ya existe para esta enfermedad.

---

## 11. Declaración de alcance

Análisis computacional de investigación presentado a un reto. **No realizado bajo acreditación
clínica ni de laboratorio.** Ninguna variante, mecanismo o candidato descrito tiene confirmación
ortogonal. **Ninguno de estos medicamentos debe administrarse a este niño, ni a ningún paciente con
MVA, sobre la base de este documento.** Cada candidato es una hipótesis cuyo siguiente paso es un
experimento de laboratorio sobre células derivadas del paciente y, solo si esos tienen éxito, la ruta
normal de comité de ética, consulta regulatoria y diseño formal de ensayo, conducida por el equipo
clínico tratante.

---

## 12. Reproducibilidad

Todo el código y los recursos derivados de fuentes públicas están en
https://github.com/tlondonoz/RarekidMVA (40 ficheros). **No contiene datos de secuencia del
paciente** — ni VCF, ni FASTQ, ni BAM, ni tablas de genotipo a escala de genoma — por los términos
del dataset y por tratarse del genoma de un menor real. `DATA_AVAILABILITY.md` documenta cada
exclusión; todo es regenerable con el código más el dataset, que el jurado posee.

Fuentes públicas usadas: PubMed (E-utilities), openFDA Drugs@FDA y etiquetas SPL, Open Targets
GraphQL, UniProt (O60566 y 247 ortólogos de vertebrados), AlphaFold DB (AF-O60566), RCSB
PDB (6TLJ, 5KHU), RefSeq NM_001211.6, y los registros públicos de la EMA y la Comisión Europea.
Software: Biopython (PairwiseAligner con BLOSUM62, SASA de Shrake-Rupley), NumPy, pandas, matplotlib.
