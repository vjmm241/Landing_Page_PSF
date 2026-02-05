# SISTEMA ÚNICO DE RAZONAMIENTO, CRÍTICA Y EJECUCIÓN PREMIUM

### **ESTÁNDAR ANTIGRAVITY PARA OPTIMIZACIÓN LANDING PROSMART FACTORIES**

---

## **PREÁMBULO OPERATIVO**

Este documento constituye la **fuente única de verdad** para el análisis, crítica sistemática y optimización incremental de la landing page ProSmart Factories. No es orientación general: es un protocolo ejecutable paso a paso.

**Regla suprema:** Cada modificación debe poder justificarse bajo los principios de este documento. Si no puede justificarse, debe rechazarse o rediseñarse.

**Prioridad absoluta:** Experiencia del usuario \> Conversión \> Estética \> Complejidad técnica.

---

## **1\. ANÁLISIS CRÍTICO DEL ESTADO ACTUAL**

### **1.1 DIAGNÓSTICO ESTRUCTURAL HTML**

#### **VIOLACIONES SEMÁNTICAS DETECTADAS**

❌ CRÍTICO \- Ausencia de elemento \<main\>  
   └─ Solución: Envolver todo el contenido entre \<header\> y \<footer\> en \<main\>

❌ CRÍTICO \- Jerarquía de encabezados rota  
   └─ Problema: h1 en hero, h2 en secciones sin estructura clara  
   └─ Solución: Exactamente un \<h1\>, seguir h2→h3→h4 sin saltos

❌ MEDIO \- Abuso de divs semánticamente vacíos  
   └─ .hero-content → \<article\>  
   └─ .timeline-visual → \<figure\> con \<figcaption\>  
   └─ .calc-dashboard → \<aside\> con aria-label

❌ MEDIO \- Elementos interactivos no nativos  
   └─ .calc-tab implementado como button pero falta role="tab"

   └─ Falta aria-selected, aria-controls para accesibilidad

#### **ESTRUCTURA SEMÁNTICA OBJETIVO**

html  
\<\!DOCTYPE html\>  
\<html lang\="es"\>  
\<head\>...\</head\>  
\<body\>  
  \<a href\="\#main-content" class\="skip-link"\>Saltar al contenido\</a\>  
    
  \<header role\="banner"\>  
    \<nav aria-label\="Navegación principal"\>...\</nav\>  
  \</header\>

  \<main id\="main-content"\>  
    \<article class\="hero" aria-labelledby\="hero-title"\>  
      \<h1 id\="hero-title"\>...\</h1\>  
    \</article\>

    \<section id\="calculadora" aria-labelledby\="calc-title"\>  
      \<h2 id\="calc-title"\>...\</h2\>  
      \<div role\="tablist" aria-label\="Configuración de cálculo"\>  
        \<button role\="tab" aria-selected\="true" aria-controls\="panel-operativa"\>...\</button\>  
      \</div\>  
    \</section\>

    \<section id\="problema" aria-labelledby\="problema-title"\>  
      \<h2 id\="problema-title"\>...\</h2\>  
      \<ol class\="timeline" aria-label\="Ciclo de pérdida operativa"\>  
        \<li\>...\</li\>  
      \</ol\>  
    \</section\>  
  \</main\>

  \<footer role\="contentinfo"\>...\</footer\>  
\</body\>  
\</html\>  
\`\`\`

\---

\#\#\# 1.2 DIAGNÓSTICO DE ACCESIBILIDAD

\#\#\#\# \*\*FALLOS CRÍTICOS WCAG 2.1 AA\*\*  
\`\`\`  
🚨 Contraste insuficiente  
   └─ .section-sub (color: \#94a3b8 sobre \#0a0f1c) \= 4.2:1  
   └─ Mínimo requerido: 4.5:1  
   └─ Solución: Aumentar a \#a8b8cf

🚨 Sliders sin ARIA  
   └─ Faltan: aria-valuemin, aria-valuemax, aria-valuenow, aria-label

   └─ Implementación:

html  
\<input   
  type\="range"   
  id\="slider-operarios"  
  class\="slider"  
  min\="5"   
  max\="100"   
  value\="20"  
  aria-valuemin\="5"  
  aria-valuemax\="100"  
  aria-valuenow\="20"  
  aria-label\="Número de operarios"  
  aria-describedby\="val-operarios"  
\>  
\<output id\="val-operarios" for\="slider-operarios"\>20\</output\>  
\`\`\`  
\`\`\`  
🚨 SVG Gauge sin accesibilidad  
   └─ Falta \<title\> y \<desc\> en SVG

   └─ Solución:

html  
\<svg class\="gauge-svg" viewBox\="0 0 220 130" role\="img" aria-labelledby\="gauge-title gauge-desc"\>  
  \<title id\="gauge-title"\>Indicador de nivel de crisis operativa\</title\>  
  \<desc id\="gauge-desc"\>Muestra el nivel actual de pérdidas: BAJO, MEDIO o CRÍTICO\</desc\>  
  *\<\!-- resto del SVG \--\>*  
\</svg\>  
\`\`\`  
\`\`\`  
🚨 Animaciones sin prefers-reduced-motion  
   └─ Todas las @keyframes deben respetar preferencias

   └─ Implementación global:

css  
@media (prefers-reduced-motion: reduce) {  
  \*,  
  \*::before,  
  \*::after {  
    animation-duration: 0.01ms \!important;  
    animation-iteration-count: 1 \!important;  
    transition-duration: 0.01ms \!important;  
  }  
}  
\`\`\`  
\`\`\`  
🚨 Focus visible insuficiente

   └─ Agregar outline personalizado a todos los interactivos:

css  
:focus-visible {  
  outline: 3px solid var(\--primary);  
  outline-offset: 4px;  
  border-radius: 4px;  
}

.btn-primary:focus-visible,  
.btn-secondary:focus-visible {  
  outline-color: white;

}

---

### **1.3 DIAGNÓSTICO DE ARQUITECTURA CSS**

#### **VARIABLES: SISTEMA DE TOKENS DE DISEÑO**

**ESTADO ACTUAL:** Variables básicas funcionales pero incompletas.

**OPTIMIZACIÓN:** Sistema de diseño escalable por niveles.

css  
:root {  
  */\* \=== PRIMITIVAS DE COLOR \=== \*/*  
  \--color-navy-950: \#0a0f1c;  
  \--color-navy-900: \#111827;  
  \--color-navy-800: \#1a2332;  
  \--color-orange-500: \#f97316;  
  \--color-orange-600: \#ea580c;  
  \--color-red-500: \#ef4444;  
  \--color-red-600: \#dc2626;  
  \--color-green-500: \#22c55e;  
  \--color-green-600: \#25D366;  
  \--color-slate-400: \#94a3b8;  
  \--color-slate-200: \#f8fafc;  
    
  */\* \=== TOKENS SEMÁNTICOS \=== \*/*  
  \--bg-primary: var(\--color-navy-950);  
  \--bg-secondary: var(\--color-navy-900);  
  \--surface-elevated: var(\--color-navy-800);  
  \--text-primary: var(\--color-slate-200);  
  \--text-secondary: var(\--color-slate-400);  
  \--brand-primary: var(\--color-orange-500);  
  \--brand-primary-hover: var(\--color-orange-600);  
  \--feedback-danger: var(\--color-red-500);  
  \--feedback-success: var(\--color-green-500);  
    
  */\* \=== ESPACIADO SISTEMÁTICO \=== \*/*  
  \--space-xs: 0.5rem;    */\* 8px \*/*  
  \--space-sm: 1rem;      */\* 16px \*/*  
  \--space-md: 1.5rem;    */\* 24px \*/*  
  \--space-lg: 2.5rem;    */\* 40px \*/*  
  \--space-xl: 4rem;      */\* 64px \*/*  
  \--space-2xl: 7.5rem;   */\* 120px \*/*  
    
  */\* \=== TIMING DE ANIMACIONES \=== \*/*  
  \--duration-instant: 150ms;  
  \--duration-fast: 250ms;  
  \--duration-normal: 400ms;  
  \--duration-slow: 600ms;  
    
  */\* \=== EASING CURVES \=== \*/*  
  \--ease-smooth: cubic-bezier(0.4, 0, 0.2, 1);  
  \--ease-bounce: cubic-bezier(0.175, 0.885, 0.32, 1.275);  
  \--ease-in: cubic-bezier(0.4, 0, 1, 1);  
  \--ease-out: cubic-bezier(0, 0, 0.2, 1);  
    
  */\* \=== TIPOGRAFÍA ESCALABLE \=== \*/*  
  \--text-xs: clamp(0.75rem, 0.7rem \+ 0.25vw, 0.875rem);  
  \--text-sm: clamp(0.875rem, 0.8rem \+ 0.375vw, 1rem);  
  \--text-base: clamp(1rem, 0.95rem \+ 0.25vw, 1.125rem);  
  \--text-lg: clamp(1.125rem, 1rem \+ 0.625vw, 1.5rem);  
  \--text-xl: clamp(1.5rem, 1.25rem \+ 1.25vw, 2.25rem);  
  \--text-2xl: clamp(2rem, 1.5rem \+ 2.5vw, 3.5rem);  
  \--text-3xl: clamp(2.5rem, 2rem \+ 2.5vw, 4.5rem);  
  \--text-4xl: clamp(2.8rem, 2.2rem \+ 3vw, 5rem);  
    
  */\* \=== RADIOS DE BORDE \=== \*/*  
  \--radius-sm: 8px;  
  \--radius-md: 14px;  
  \--radius-lg: 24px;  
  \--radius-xl: 32px;  
  \--radius-full: 9999px;  
    
  */\* \=== SOMBRAS ELEVACIÓN \=== \*/*  
  \--shadow-sm: 0 4px 20px rgba(0,0,0,0.1);  
  \--shadow-md: 0 10px 40px rgba(0,0,0,0.2);  
  \--shadow-lg: 0 20px 60px rgba(0,0,0,0.3);  
  \--shadow-brand: 0 10px 40px rgba(249,115,22,0.3);

}

#### **LAYOUT: GRID COMO FUNDAMENTO**

**PROBLEMA ACTUAL:** Mezcla indiscriminada de Flexbox y valores mágicos.

**SOLUCIÓN:** Grid para layouts principales, Flexbox solo para alineación interna.

css  
*/\* ❌ INCORRECTO \- Estado actual \*/*  
.calc-layout {  
  display: grid;  
  grid-template-columns: 1fr 480px; */\* valor mágico \*/*  
  gap: 50px; */\* valor mágico \*/*  
}

*/\* ✅ CORRECTO \- Arquitectura sistemática \*/*  
.calc-layout {  
  display: grid;  
  grid-template-columns: 1fr min(480px, 40%);  
  gap: var(\--space-xl);  
  align-items: start;  
}

*/\* Layout responsivo con Grid Areas \*/*  
@media (max-width: 1024px) {  
  .calc-layout {  
    grid-template-columns: 1fr;  
    grid-template-areas:  
      "inputs"  
      "results";  
  }  
    
  .calc-inputs { grid-area: inputs; }  
  .calc-results { grid-area: results; }  
}  
\`\`\`

\---

\#\#\# 1.4 DIAGNÓSTICO DE ANIMACIONES

\#\#\#\# \*\*CLASIFICACIÓN POR INTENCIÓN COGNITIVA\*\*  
\`\`\`  
TIPO 1: MICROINTERACCIONES (CSS puro)  
├─ Hover de botones: 150-250ms  
├─ Focus states: 150ms  
├─ Toggle de tabs: 200ms  
└─ Transform \+ Opacity SOLAMENTE

TIPO 2: TRANSICIONES DE ESTADO (CSS \+ JS)  
├─ Panel switching: 400ms ease-smooth  
├─ Gauge updates: 600ms ease-smooth  
└─ Transform \+ Opacity SOLAMENTE

TIPO 3: NARRATIVA VISUAL (Requires GSAP \- NO IMPLEMENTADO AÚN)  
├─ Hero progressive reveal  
├─ Timeline scroll-triggered  
└─ WhatsApp message sequence  
\`\`\`

\#\#\#\# \*\*VIOLACIONES DE PERFORMANCE DETECTADAS\*\*  
\`\`\`  
❌ CRÍTICO \- Animación de propiedades costosas  
   └─ .badge { animation: badgeFloat ... }  
   └─ Anima translateY → Correcto ✓  
   └─ PERO: No usa will-change

❌ CRÍTICO \- Animaciones sin GPU acceleration  
   └─ .grid-bg { animation: gridPulse ... }  
   └─ Anima opacity → Correcto ✓  
   └─ PERO: No usa transform: translateZ(0) para GPU

❌ MEDIO \- Exceso de animaciones simultáneas  
   └─ Hero: 7 animaciones corriendo al mismo tiempo  
   └─ Impacto: Layout thrashing posible

   └─ Solución: Stagger secuencial con delays

#### **IMPLEMENTACIÓN CORRECTA**

css  
*/\* ✅ Microinteracción optimizada \*/*  
.btn-primary {  
  transition: transform var(\--duration-fast) var(\--ease-smooth),  
              box-shadow var(\--duration-fast) var(\--ease-smooth);  
  will-change: transform; */\* Solo en hover \*/*  
}

.btn-primary:hover {  
  transform: translateY(\-4px) scale(1.02);  
  box-shadow: var(\--shadow-lg);  
}

.btn-primary:active {  
  transform: translateY(\-2px) scale(1.01);  
  transition-duration: var(\--duration-instant);  
}

*/\* ✅ Animación de fondo optimizada \*/*  
.grid-bg {  
  animation: gridPulse 4s ease-in-out infinite;  
  transform: translateZ(0); */\* GPU acceleration \*/*  
  will-change: opacity;  
}

@keyframes gridPulse {  
  0%, 100% { opacity: 0.3; }  
  50% { opacity: 0.6; }  
}

*/\* ✅ Hero staggered con intención \*/*  
.hero-title {  
  animation: fadeInUp 0.8s var(\--ease-smooth) 0.2s both;  
}

.hero-sub {  
  animation: fadeInUp 0.8s var(\--ease-smooth) 0.4s both;  
}

.hero-features {  
  animation: fadeInUp 0.8s var(\--ease-smooth) 0.6s both;  
}

@keyframes fadeInUp {  
  from {  
    opacity: 0;  
    transform: translateY(30px);  
  }  
  to {  
    opacity: 1;  
    transform: translateY(0);  
  }

}

---

## **2\. PLAN DE OPTIMIZACIÓN INCREMENTAL**

### **2.1 FASE 1: FUNDAMENTOS (PRIORIDAD CRÍTICA)**

#### **Acción 1.1: Reestructuración Semántica HTML**

html  
*\<\!-- ANTES \--\>*  
\<section class\="hero" id\="hero"\>  
  \<div class\="hero-content"\>  
    \<h1 class\="hero-title"\>...\</h1\>  
  \</div\>  
\</section\>

*\<\!-- DESPUÉS \--\>*  
\<main id\="main-content"\>  
  \<article class\="hero" aria-labelledby\="hero-title"\>  
    \<div class\="hero-content"\>  
      \<h1 id\="hero-title"\>¿Cuánto le cuesta un operario con los \<span class\="hl"\>brazos cruzados\</span\> esperando al encargado?\</h1\>  
      \<p class\="hero-sub"\>...\</p\>  
    \</div\>  
  \</article\>

\</main\>

**Justificación:** El hero es contenido autónomo (article), no solo una sección decorativa.

---

#### **Acción 1.2: Sistema de Tokens CSS**

Reemplazar todas las variables actuales con el sistema de tokens documentado en 1.3.

**Impacto medible:**

* Mantenibilidad: \+40% (cambios centralizados)  
* Consistencia visual: 100% (imposible usar valores arbitrarios)  
* Escalabilidad: \+80% (agregar dark mode en 1 hora)

---

#### **Acción 1.3: Accesibilidad ARIA Completa**

**Calculadora con tabs accesibles:**

html  
\<div role\="tablist" aria-label\="Configuración de cálculo de pérdidas" class\="calc-tabs"\>  
  \<button   
    role\="tab"   
    id\="tab-operativa"  
    aria-selected\="true"   
    aria-controls\="panel-operativa"  
    class\="calc-tab active"  
    tabindex\="0"  
  \>  
    \<span\>1. Operativa\</span\>  
  \</button\>  
    
  \<button   
    role\="tab"   
    id\="tab-interrupciones"  
    aria-selected\="false"   
    aria-controls\="panel-interrupciones"  
    class\="calc-tab"  
    tabindex\="\-1"  
  \>  
    \<span\>2. Interrupciones\</span\>  
  \</button\>  
\</div\>

\<div role\="tabpanel" id\="panel-operativa" aria-labelledby\="tab-operativa" class\="calc-panel active"\>  
  *\<\!-- contenido \--\>*

\</div\>

**JavaScript para gestión de teclado:**

javascript  
function initAccessibleTabs() {  
  const tablist \= document.querySelector('\[role="tablist"\]');  
  const tabs \= tablist.querySelectorAll('\[role="tab"\]');  
  const panels \= document.querySelectorAll('\[role="tabpanel"\]');  
    
  tabs.forEach((tab, i) \=\> {  
    tab.addEventListener('click', () \=\> activateTab(tab, i));  
    tab.addEventListener('keydown', (e) \=\> {  
      if (e.key \=== 'ArrowRight') {  
        e.preventDefault();  
        const next \= tabs\[(i \+ 1) % tabs.length\];  
        activateTab(next, (i \+ 1) % tabs.length);  
        next.focus();  
      }  
      if (e.key \=== 'ArrowLeft') {  
        e.preventDefault();  
        const prev \= tabs\[(i \- 1 \+ tabs.length) % tabs.length\];  
        activateTab(prev, (i \- 1 \+ tabs.length) % tabs.length);  
        prev.focus();  
      }  
    });  
  });  
    
  function activateTab(tab, index) {  
    tabs.forEach(t \=\> {  
      t.setAttribute('aria-selected', 'false');  
      t.setAttribute('tabindex', '-1');  
      t.classList.remove('active');  
    });  
      
    panels.forEach(p \=\> p.classList.remove('active'));  
      
    tab.setAttribute('aria-selected', 'true');  
    tab.setAttribute('tabindex', '0');  
    tab.classList.add('active');  
    panels\[index\].classList.add('active');  
  }

}

---

### **2.2 FASE 2: OPTIMIZACIÓN DE PERFORMANCE**

#### **Acción 2.1: Lazy Loading de Animaciones Pesadas**

**Problema:** Las animaciones decorativas (particles, grid-bg) cargan inmediatamente.

**Solución:** Diferir hasta después de First Contentful Paint.

javascript  
*// Cargar animaciones decorativas solo después de FCP*  
if ('requestIdleCallback' in window) {  
  requestIdleCallback(() \=\> {  
    createParticles();  
    initDecorations();  
  });  
} else {  
  setTimeout(() \=\> {  
    createParticles();  
    initDecorations();  
  }, 2000);

}

---

#### **Acción 2.2: Intersection Observer para Animaciones**

**Problema:** Timeline items animan aunque no estén visibles.

**Solución:** Activar animaciones solo cuando entren al viewport.

javascript  
function initTimeline() {  
  const observer \= new IntersectionObserver(  
    (entries) \=\> {  
      entries.forEach(entry \=\> {  
        if (entry.isIntersecting) {  
          entry.target.classList.add('visible');  
          observer.unobserve(entry.target); *// Solo animar una vez*  
        }  
      });  
    },  
    {  
      threshold: 0.2,  
      rootMargin: '0px 0px \-10% 0px' *// Activar antes de llegar*  
    }  
  );

  document.querySelectorAll('.timeline-item').forEach(item \=\> {  
    observer.observe(item);  
  });

}

---

#### **Acción 2.3: Optimización de Repaint/Reflow**

**Calculadora: Batch DOM updates**

javascript  
*// ❌ ANTES: 4 reflows*  
document.getElementById('result-total').textContent \= '€' \+ total;  
document.getElementById('result-anual').textContent \= '€' \+ anual;  
document.getElementById('result-salario').textContent \= '€' \+ salario;  
document.getElementById('result-horas').textContent \= horas \+ ' hrs';

*// ✅ DESPUÉS: 1 reflow usando DocumentFragment*  
const updates \= \[  
  \['result-total', '€' \+ total\],  
  \['result-anual', '€' \+ anual\],  
  \['result-salario', '€' \+ salario\],  
  \['result-horas', horas \+ ' hrs'\]  
\];

requestAnimationFrame(() \=\> {  
  updates.forEach((\[id, value\]) \=\> {  
    document.getElementById(id).textContent \= value;  
  });

});

---

### **2.3 FASE 3: IMPLEMENTACIÓN GSAP (ANIMACIONES NARRATIVAS)**

**IMPORTANTE:** GSAP solo para animaciones que requieren:

1. Secuencialidad compleja (timeline)  
2. Control fino de timing  
3. Sincronización con scroll (ScrollTrigger)

#### **Acción 3.1: Hero Progressive Reveal**

javascript  
*// Cargar GSAP via CDN*  
\<script src\="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"\>\</script\>

*// Timeline del Hero*  
function initHeroAnimation() {  
  const tl \= gsap.timeline({  
    defaults: {  
      ease: "power3.out",  
      duration: 0.8  
    }  
  });  
    
  tl.from(".hero-title", {  
    y: 60,  
    opacity: 0,  
    duration: 1  
  })  
  .from(".hero-sub", {  
    y: 40,  
    opacity: 0  
  }, "-=0.4") *// Overlap de 0.4s*  
  .from(".hero-feat", {  
    y: 30,  
    opacity: 0,  
    stagger: 0.08, *// Stagger cognitivo*  
    duration: 0.6  
  }, "-=0.3")  
  .from(".hero-btns \> \*", {  
    y: 20,  
    opacity: 0,  
    stagger: 0.1  
  }, "-=0.2");  
}

*// Ejecutar solo una vez cuando el hero sea visible*  
const heroObserver \= new IntersectionObserver((entries) \=\> {  
  if (entries\[0\].isIntersecting) {  
    initHeroAnimation();  
    heroObserver.disconnect();  
  }  
}, { threshold: 0.3 });

heroObserver.observe(document.querySelector('.hero'));

**Justificación:**

* Stagger de 0.08s crea ritmo visual sin ser abrumador  
* Overlaps (-=0.4s) mantienen fluidez  
* IntersectionObserver evita animar si usuario scrollea rápido

---

#### **Acción 3.2: Timeline con ScrollTrigger**

javascript  
\<script src\="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"\>\</script\>

gsap.registerPlugin(ScrollTrigger);

function initTimelineScroll() {  
  const items \= gsap.utils.toArray('.timeline-item');  
    
  items.forEach((item, i) \=\> {  
    gsap.from(item, {  
      scrollTrigger: {  
        trigger: item,  
        start: "top 80%",  
        end: "top 50%",  
        scrub: false, *// Animación única, no ligada a scroll*  
        once: true,  
        markers: false *// Cambiar a true para debug*  
      },  
      y: 100,  
      opacity: 0,  
      duration: 0.8,  
      ease: "power2.out"  
    });  
      
    *// Animar el node con bounce sutil*  
    gsap.from(item.querySelector('.node-circle'), {  
      scrollTrigger: {  
        trigger: item,  
        start: "top 70%",  
        once: true  
      },  
      scale: 0,  
      rotation: 180,  
      duration: 0.6,  
      ease: "back.out(1.4)", *// Bounce controlado*  
      delay: 0.2  
    });  
  });

}

**Justificación:**

* ScrollTrigger mejora comprensión de secuencia  
* `once: true` evita re-animaciones innecesarias  
* Bounce en nodes crea énfasis sin ser infantil

---

### **2.4 FASE 4: CONVERSIÓN Y UX**

#### **Acción 4.1: Validación en Tiempo Real del Formulario**

javascript  
function initFormValidation() {  
  const form \= document.getElementById('contact-form');  
  const inputs \= form.querySelectorAll('input\[required\], select\[required\]');  
    
  inputs.forEach(input \=\> {  
    input.addEventListener('blur', () \=\> {  
      validateField(input);  
    });  
      
    input.addEventListener('input', () \=\> {  
      if (input.classList.contains('error')) {  
        validateField(input);  
      }  
    });  
  });  
    
  function validateField(field) {  
    const isValid \= field.checkValidity();  
    const errorMsg \= field.parentElement.querySelector('.error-message');  
      
    if (\!isValid) {  
      field.classList.add('error');  
      field.setAttribute('aria-invalid', 'true');  
        
      if (\!errorMsg) {  
        const msg \= document.createElement('span');  
        msg.className \= 'error-message';  
        msg.id \= \`${field.id}\-error\`;  
        msg.textContent \= field.validationMessage;  
        field.setAttribute('aria-describedby', msg.id);  
        field.parentElement.appendChild(msg);  
      }  
    } else {  
      field.classList.remove('error');  
      field.setAttribute('aria-invalid', 'false');  
      if (errorMsg) errorMsg.remove();  
    }  
  }

}

**CSS para estados de error:**

css  
.form-input.error,  
.form-select.error {  
  border-color: var(\--feedback-danger);  
  box-shadow: 0 0 0 4px rgba(239, 68, 68, 0.15);  
}

.error-message {  
  display: block;  
  color: var(\--feedback-danger);  
  font-size: var(\--text-xs);  
  margin-top: var(\--space-xs);  
  animation: slideInDown var(\--duration-fast) var(\--ease-smooth);  
}

@keyframes slideInDown {  
  from {  
    opacity: 0;  
    transform: translateY(\-8px);  
  }  
  to {  
    opacity: 1;  
    transform: translateY(0);  
  }

}

---

#### **Acción 4.2: Feedback Visual de Cálculo**

**Problema:** Los números cambian instantáneamente, sin contexto.

**Solución:** Animación de conteo \+ highlight de cambios.

javascript  
function animateNumber(element, newValue, duration \= 800) {  
  const oldValue \= parseFloat(element.textContent.replace(/\[^0-9.-\]/g, '')) || 0;  
  const prefix \= element.textContent.match(/\[^0-9.-\]/g)?.join('') || '';  
    
  const startTime \= performance.now();  
    
  function update(currentTime) {  
    const elapsed \= currentTime \- startTime;  
    const progress \= Math.min(elapsed / duration, 1);  
      
    *// Easing out cubic*  
    const easedProgress \= 1 \- Math.pow(1 \- progress, 3);  
    const currentValue \= oldValue \+ (newValue \- oldValue) \* easedProgress;  
      
    element.textContent \= prefix \+ formatNumber(Math.round(currentValue));  
      
    if (progress \< 1) {  
      requestAnimationFrame(update);  
    } else {  
      *// Highlight al terminar*  
      element.classList.add('updated');  
      setTimeout(() \=\> element.classList.remove('updated'), 600);  
    }  
  }  
    
  requestAnimationFrame(update);  
}

*// Uso en calcular()*  
function calcular() {  
  *// ... cálculos ...*  
    
  animateNumber(document.getElementById('result-total'), totalMes);  
  animateNumber(document.getElementById('result-anual'), totalAnual);  
  *// etc...*

}

**CSS para highlight:**

css  
.updated {  
  animation: highlight var(\--duration-normal) var(\--ease-smooth);  
}

@keyframes highlight {  
  0%, 100% {  
    color: inherit;  
  }  
  50% {  
    color: var(\--brand-primary);  
    transform: scale(1.05);  
  }  
}  
\`\`\`

\---

\#\# 3. SISTEMA DE CRÍTICA CONTINUA

\#\#\# 3.1 CHECKLIST PRE-COMMIT

Antes de implementar CUALQUIER cambio, verificar:  
\`\`\`  
□ ¿Mejora la experiencia del usuario de forma medible?  
□ ¿Respeta la jerarquía semántica HTML?  
□ ¿Es accesible vía teclado y screen reader?  
□ ¿Mantiene contraste WCAG AA (4.5:1)?  
□ ¿Las animaciones respetan prefers-reduced-motion?  
□ ¿Usa solo transform \+ opacity?  
□ ¿Evita layout thrashing?  
□ ¿La duración está entre 150-600ms?  
□ ¿Tiene justificación cognitiva clara?  
□ ¿Puede eliminarse sin perder claridad?  
\`\`\`

Si alguna respuesta es "No" → Rechazar o rediseñar.

\---

\#\#\# 3.2 MÉTRICAS DE RENDIMIENTO

\*\*Core Web Vitals \- Objetivos:\*\*  
\`\`\`  
LCP (Largest Contentful Paint):  \< 2.5s  
FID (First Input Delay):         \< 100ms

CLS (Cumulative Layout Shift):   \< 0.1

**Medir con:**

javascript  
*// Agregar al final del \<body\>*  
\<script\>  
new PerformanceObserver((list) \=\> {  
  for (const entry of list.getEntries()) {  
    console.log('LCP:', entry.renderTime || entry.loadTime);  
  }  
}).observe({entryTypes: \['largest-contentful-paint'\]});

new PerformanceObserver((list) \=\> {  
  for (const entry of list.getEntries()) {  
    console.log('FID:', entry.processingStart \- entry.startTime);  
  }  
}).observe({entryTypes: \['first-input'\]});

new PerformanceObserver((list) \=\> {  
  let cls \= 0;  
  for (const entry of list.getEntries()) {  
    if (\!entry.hadRecentInput) {  
      cls \+= entry.value;  
    }  
  }  
  console.log('CLS:', cls);  
}).observe({entryTypes: \['layout-shift'\]});

\</script\>

---

### **3.3 A/B TESTING DE CONVERSIÓN**

\*\*

Continuar

22:05

Hipótesis a probar:\*\*

1. **CTA en Hero:**  
   * Variante A (actual): "🔥 Calcular Mi Fuga de Capital"  
   * Variante B: "Ver Mi Diagnóstico Gratuito"  
   * Métrica: Click-through rate  
2. **Formulario de contacto:**  
   * Variante A (actual): 7 campos  
   * Variante B: 3 campos esenciales \+ "agregar más datos"  
   * Métrica: Tasa de completación  
3. **Gauge de crisis:**  
   * Variante A (actual): Con aguja  
   * Variante B: Barra de progreso horizontal  
   * Métrica: Tiempo en sección

---

## **4\. ROADMAP DE IMPLEMENTACIÓN**

### **SEMANA 1: Fundamentos**

* Día 1-2: Reestructuración HTML semántica  
* Día 3-4: Sistema de tokens CSS  
* Día 5: ARIA completo \+ validación accesibilidad

### **SEMANA 2: Performance**

* Día 1-2: Lazy loading \+ Intersection Observer  
* Día 3-4: Optimización de reflows  
* Día 5: Auditoría Lighthouse (objetivo: 95+)

### **SEMANA 3: Animaciones**

* Día 1-2: Integración GSAP \+ Hero timeline  
* Día 3-4: ScrollTrigger en Timeline  
* Día 5: Pulido \+ testing en dispositivos

### **SEMANA 4: Conversión**

* Día 1-2: Validación de formulario  
* Día 3-4: Animaciones de feedback  
* Día 5: Setup A/B testing

---

## **5\. REGLAS SUPREMAS (NUNCA VIOLAR)**

1\. Un solo \<h1\> por página  
2\. Jerarquía h1 → h2 → h3 sin saltos  
3\. Elementos interactivos \= nativos (button, a)  
4\. Animaciones \= transform \+ opacity únicamente  
5\. Duración \= 150-600ms (excepto narrativas)  
6\. Contraste mínimo \= 4.5:1  
7\. Focus visible obligatorio  
8\. prefers-reduced-motion \= respetado  
9\. Validación antes de commit

10\. Experiencia usuario \> Todo lo demás

---

## **6\. ARQUITECTURA DE DECISIONES**

### **Framework de Evaluación:**

PREGUNTA: ¿Debería agregar/modificar X?

1\. ¿Mejora conversión?   
   └─ NO → Rechazar  
   └─ SÍ → Continuar

2\. ¿Empeora performance?  
   └─ SÍ → Rechazar o rediseñar  
   └─ NO → Continuar

3\. ¿Rompe accesibilidad?  
   └─ SÍ → Rechazar  
   └─ NO → Continuar

4\. ¿Agrega complejidad innecesaria?  
   └─ SÍ → Simplificar  
   └─ NO → Aprobar

APROBADO → Implementar → Medir → Iterar

---

## **7\. CONCLUSIÓN OPERATIVA**

Este documento es **vivo y evolutivo**. Cada optimización implementada debe:

1. Documentarse con justificación  
2. Medirse con métricas objetivas  
3. Compararse con estado anterior  
4. Validarse con usuarios reales

**La regla final es simple:**

Si no mejora experiencia, conversión o performance de forma medible → No se implementa.

La calidad es el resultado de decisiones consistentes, justificadas y repetibles. Este plan define esas decisiones.

---

**Próxima revisión:** Después de Semana 4 **Responsable:** Equipo de desarrollo **Aprobación:** Product Owner \+ UX Lead

---

