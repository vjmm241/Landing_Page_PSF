---

**INSTRUCCIÓN PARA REPLICAR EXACTAMENTE LA SECCIÓN "EL COSTO DEL TIEMPO MUERTO"**

Crea una sección HTML completa con el título "ProSmart Factories \- El Costo del Tiempo Muerto" que debe seguir EXACTAMENTE estas especificaciones:

**ESTRUCTURA DE COLORES Y VARIABLES CSS:**

* Fondo principal: \#0a0f1c  
* Fondo secundario: \#111827  
* Color primario (naranja): \#f97316  
* Color peligro (rojo): \#ef4444  
* Color advertencia (amarillo): \#eab308  
* Color éxito (verde): \#22c55e  
* Color púrpura: \#a855f7  
* Texto principal: \#f8fafc  
* Texto secundario: \#94a3b8  
* Líneas: \#1e293b

**TIPOGRAFÍAS EXACTAS:**

* Títulos grandes: 'Bebas Neue' (Google Fonts)  
* Código/monospace: 'JetBrains Mono' (pesos 400 y 700\)  
* Texto general: 'Plus Jakarta Sans' (pesos 400, 500, 600, 700\)

**FONDO ANIMADO CON DOS CAPAS:**

1. **Grid industrial pulsante:** Grid de líneas naranjas (\#f97316 con opacidad 0.03), tamaño 60x60px, con animación de pulso que varía opacidad entre 0.4 y 0.8 cada 4 segundos  
2. **Partículas flotantes:** 20 partículas circulares naranjas y 8 engranajes (círculos con borde) que flotan de abajo hacia arriba con rotación. Partículas: 2-6px, opacidad 0.2, duración 15-30s. Engranajes: 20px, borde 2px, opacidad 0.1, duración 20-35s, rotación completa durante el ascenso

**HEADER DE SECCIÓN (centrado):**

* Línea superior decorativa: 80px de ancho, 4px altura, gradiente naranja horizontal que pulsa expandiéndose a 160px cada 2s  
* Badge flotante: Fondo rgba(249,115,22,0.08), borde rgba(249,115,22,0.25), padding 10px 24px, border-radius 40px, texto "ANÁLISIS CRÍTICO" en mayúsculas, 0.8rem, espaciado de letras 3px, con punto pulsante de 8px que tiene anillo expansivo  
* Título principal: "EL COSTO DEL TIEMPO MUERTO", font-size clamp(2.8rem, 7vw, 5rem), Bebas Neue, espaciado 4px, gradiente animado que va de blanco a naranja a rojo cada 5s con background-clip: text  
* Subtítulo: 1.15rem, color texto secundario, max-width 650px, centrado

**TIMELINE CENTRAL CON LÍNEA VERTICAL:**

* Línea central: 3px de ancho, centrada, gradiente vertical que empieza transparente, color línea en medio, termina transparente  
* Pulso de energía: Gradiente naranja-amarillo que recorre la línea de arriba a abajo en loop infinito de 3s con blur de 20px  
* Nodos en la línea: 4 nodos circulares de 80px con:  
  * Anillo exterior pulsante naranja (scale 1 a 1.2, opacidad 0.3 a 0\)  
  * Círculo medio giratorio con gradiente cónico naranja-amarillo  
  * Centro sólido naranja de 40px  
  * Icono SVG en el centro (engranaje, reloj, alerta, gráfico)  
  * Hover: escala 1.1, brillo aumenta

**4 TARJETAS DE CONTENIDO (alternando izquierda-derecha):**

**Tarjeta 1 \- "Máquina Parada" (izquierda):**

* Card con fondo secundario, border 1px línea, border-radius 24px, padding 40px  
* Efecto 3D al hover: rotación perspective según posición del mouse  
* Badge superior: "ESCENARIO 1", fondo semi-transparente naranja  
* Título: "Máquina Parada", 2rem, Plus Jakarta Sans  
* Párrafo descriptivo: 1.05rem, line-height 1.8, color texto secundario  
* Grid de 3 métricas con iconos:  
  * "⏱️ 12 min promedio" (amarillo)  
  * "📉 \-8% producción" (rojo)  
  * "💰 €127/hora perdidos" (naranja)  
* Visualización: Máquina en paro con animación de humo, reloj digital con cronómetro corriendo desde 09:40 hasta 15:00 en loop, barra de progreso roja que se llena

**Tarjeta 2 \- "Espera de Material" (derecha):**

* Badge: "ESCENARIO 2"  
* Título: "Espera de Material"  
* Métricas:  
  * "⏳ 18 min espera" (amarillo)  
  * "📊 \-12% eficiencia" (rojo)  
  * "💸 €340/hora perdidos" (naranja)  
* Visualización: Cinta transportadora vacía con iconos de cajas desvanecidas, barra de stock vacía con animación de "AGOTADO" parpadeante, contador de tiempo en espera

**Tarjeta 3 \- "Fallo de Calidad" (izquierda):**

* Badge: "ESCENARIO 3"  
* Título: "Fallo de Calidad"  
* Métricas:  
  * "🔴 35 min pérdida" (rojo)  
  * "❌ Lote completo" (rojo)  
  * "💀 €890/hora perdidos" (rojo)  
* Visualización: Productos con X roja, animación de productos cayendo al scrap, contador de unidades defectuosas que aumenta

**Tarjeta 4 \- "Parálisis por Análisis" (derecha):**

* Badge: "ESCENARIO 4"  
* Título: "Parálisis por Análisis"  
* Métricas:  
  * "🤔 45+ min perdidos" (púrpura)  
  * "📉 Decisión tardía" (rojo)  
  * "🔥 €1,200/hora perdidos" (rojo)  
* Visualización: Billetes de dinero en llamas con animación de fuego realista, humo ascendente, contador de pérdidas que incrementa de 0 a 127 cada minuto con símbolo €

**SECCIÓN CTA FINAL:**

* Título: "¿Cuánto Dinero Pierdes Cada Mes?", 2.2rem, blanco  
* Subtítulo: "Calcula el impacto real del tiempo muerto en tu fábrica"  
* Botón naranja: "Calcular Mis Pérdidas" con flecha, efecto glow y hover con escala 1.05  
* Grid de 3 estadísticas animadas (contador ascendente al hacer scroll visible):  
  * "47 Horas perdidas/mes"  
  * "€8,500 Dinero evaporado"  
  * "230 Unidades no producidas"  
  * Cada stat tiene fondo con border, padding 32px, números grandes (2.8rem) naranjas que cuentan desde 0

**ANIMACIONES Y EFECTOS JAVASCRIPT:**

1. Generación dinámica de partículas flotantes con posiciones y delays aleatorios  
2. Contador de pérdidas que incrementa de 0 a 127 cada segundo  
3. Timer que corre de 09:40 a 15:00 en loop continuo  
4. Cards con efecto 3D perspectiva al mover el mouse  
5. Nodos con efecto ripple al hacer click  
6. Estadísticas que animan al hacer scroll visible (IntersectionObserver)  
7. Todas las animaciones deben ser suaves con ease-in-out

**RESPONSIVE:**

* Max-width contenedor: 1200px  
* Padding general: 80px 20px  
* Timeline alterna izquierda-derecha en desktop  
* En mobile (\<768px): timeline lineal, cards una debajo de otra

Replica TODO exactamente como está descrito. No cambies nombres, colores, tamaños, animaciones ni estructura. La precisión es CRÍTICA.

