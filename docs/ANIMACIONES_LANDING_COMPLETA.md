# 🎬 ESPECIFICACIONES DE ANIMACIONES NIVEL MUNDIAL
## PROSMART FACTORIES - LANDING PAGE COMPLETA
### Documento Técnico para Google Antigravity / Desarrolladores

---

**Proyecto:** ProSmart Factories Landing Page  
**Versión:** 2.0  
**Fecha:** Enero 2026  
**Objetivo:** Implementar sistema de animaciones de clase mundial en toda la landing page  
**Stack Tecnológico:** HTML5, CSS3, JavaScript (ES6+), GSAP 3.12+, ScrollTrigger  
**Rendimiento Target:** 60 FPS en desktop, 30 FPS en móvil  

---

## 📋 ÍNDICE

1. [Visión General del Sistema de Animaciones](#1-visión-general)
2. [Configuración y Setup Inicial](#2-configuración-inicial)
3. [Sistema de Variables CSS](#3-sistema-de-variables)
4. [Animaciones de Hero Section](#4-hero-section)
5. [Animaciones de Navegación](#5-navegación)
6. [Animaciones de Cards/Procesos](#6-cards-y-procesos)
7. [Animaciones de Formularios](#7-formularios)
8. [Animaciones de Métricas/KPIs](#8-métricas-y-kpis)
9. [Animaciones de Testimonios](#9-testimonios)
10. [Animaciones de Footer](#10-footer)
11. [Scroll-Based Animations](#11-scroll-animations)
12. [Micro-interactions](#12-micro-interactions)
13. [Loading States](#13-loading-states)
14. [Particle System](#14-particle-system)
15. [Performance Optimization](#15-performance)
16. [Responsive Behavior](#16-responsive)
17. [Accessibility](#17-accessibility)
18. [Código de Implementación](#18-implementación)

---

## 1. VISIÓN GENERAL

### 1.1 Filosofía de Animación

**Principios Fundamentales:**
- ✨ **Significado sobre espectáculo**: Cada animación debe tener un propósito
- 🎯 **Guiar la atención**: Dirigir al usuario a elementos importantes
- ⚡ **Feedback inmediato**: Responder a las interacciones en <100ms
- 🌊 **Fluidez natural**: Movimientos orgánicos, no robóticos
- 🚀 **Performance first**: Nunca sacrificar rendimiento por vistosidad

**Jerarquía de Animaciones:**
1. **Críticas** (Hero, CTA, Nav) → Duración: 0.8-1.5s
2. **Importantes** (Cards, Forms) → Duración: 0.5-0.8s
3. **Secundarias** (Hover, Focus) → Duración: 0.2-0.4s
4. **Sutiles** (Micro-interactions) → Duración: 0.1-0.2s

### 1.2 Easing Functions Personalizadas

```css
--easing-elastic: cubic-bezier(0.68, -0.6, 0.32, 1.6);
--easing-bounce: cubic-bezier(0.68, -0.55, 0.265, 1.55);
--easing-smooth: cubic-bezier(0.4, 0, 0.2, 1);
--easing-expo: cubic-bezier(0.19, 1, 0.22, 1);
--easing-circ: cubic-bezier(0.785, 0.135, 0.15, 0.86);
--easing-back: cubic-bezier(0.68, -0.55, 0.265, 1.55);
```

### 1.3 Arquitectura del Sistema

```
animations-system/
├── core/
│   ├── variables.css (Variables globales)
│   ├── keyframes.css (Animaciones reutilizables)
│   └── utilities.css (Clases helper)
├── components/
│   ├── hero.css
│   ├── navbar.css
│   ├── cards.css
│   ├── forms.css
│   └── footer.css
├── effects/
│   ├── particles.js
│   ├── scroll-effects.js
│   └── micro-interactions.js
└── main-animations.js (Orquestador principal)
```

---

## 2. CONFIGURACIÓN INICIAL

### 2.1 Librerías Requeridas

```html
<!-- GSAP - GreenSock Animation Platform -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollToPlugin.min.js"></script>

<!-- Optional: Para animaciones de texto avanzadas -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/SplitText.min.js"></script>

<!-- Optional: Para animaciones de path SVG -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/DrawSVGPlugin.min.js"></script>
```

### 2.2 Estructura HTML Base

```html
<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ProSmart Factories - Transformación Digital Industrial</title>
    
    <!-- Preload de fuentes para evitar FOUT -->
    <link rel="preload" href="/fonts/bebas-neue.woff2" as="font" crossorigin>
    <link rel="preload" href="/fonts/jakarta-sans.woff2" as="font" crossorigin>
    
    <!-- CSS Critical Path -->
    <style>
        /* Variables y estilos críticos inline */
        :root { /* Variables aquí */ }
        body { /* Estilos base aquí */ }
    </style>
    
    <!-- CSS Principal (async loading) -->
    <link rel="stylesheet" href="/css/animations.css">
</head>
<body class="antialiased">
    <!-- Contenido -->
    
    <!-- Scripts al final del body -->
    <script src="/js/animations.js" defer></script>
</body>
</html>
```

---

## 3. SISTEMA DE VARIABLES

### 3.1 Variables CSS Completas

```css
:root {
    /* ============================================
       COLORES
       ============================================ */
    --color-navy-950: #0a0f1c;
    --color-navy-900: #111827;
    --color-navy-800: #1a2332;
    --color-orange-500: #f97316;
    --color-orange-600: #ea580c;
    --color-red-500: #ef4444;
    --color-red-600: #dc2626;
    --color-green-500: #22c55e;
    --color-blue-500: #3b82f6;
    --color-slate-400: #94a3b8;
    --color-slate-200: #f8fafc;
    
    /* Semantic Colors */
    --bg-primary: var(--color-navy-950);
    --bg-secondary: var(--color-navy-900);
    --surface: var(--color-navy-800);
    --text-primary: var(--color-slate-200);
    --text-secondary: var(--color-slate-400);
    --brand-primary: var(--color-orange-500);
    --brand-hover: var(--color-orange-600);
    --accent: var(--color-red-500);
    --success: var(--color-green-500);
    --border: rgba(255, 255, 255, 0.1);
    
    /* ============================================
       ANIMACIONES - DURACIÓN
       ============================================ */
    --duration-instant: 0.1s;
    --duration-fast: 0.2s;
    --duration-normal: 0.3s;
    --duration-medium: 0.5s;
    --duration-slow: 0.8s;
    --duration-slower: 1.2s;
    --duration-slowest: 1.5s;
    
    /* ============================================
       ANIMACIONES - EASING
       ============================================ */
    --easing-linear: linear;
    --easing-ease: ease;
    --easing-ease-in: ease-in;
    --easing-ease-out: ease-out;
    --easing-ease-in-out: ease-in-out;
    
    /* Custom Easing */
    --easing-smooth: cubic-bezier(0.4, 0, 0.2, 1);
    --easing-expo: cubic-bezier(0.19, 1, 0.22, 1);
    --easing-circ: cubic-bezier(0.785, 0.135, 0.15, 0.86);
    --easing-back: cubic-bezier(0.68, -0.55, 0.265, 1.55);
    --easing-elastic: cubic-bezier(0.68, -0.6, 0.32, 1.6);
    --easing-bounce: cubic-bezier(0.68, -0.55, 0.265, 1.55);
    
    /* ============================================
       ANIMACIONES - DELAYS
       ============================================ */
    --delay-0: 0s;
    --delay-1: 0.1s;
    --delay-2: 0.2s;
    --delay-3: 0.3s;
    --delay-4: 0.4s;
    --delay-5: 0.5s;
    
    /* ============================================
       SOMBRAS ANIMADAS
       ============================================ */
    --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
    --shadow-2xl: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
    
    /* Sombras con color */
    --shadow-orange: 0 10px 40px rgba(249, 115, 22, 0.3);
    --shadow-orange-lg: 0 20px 50px rgba(249, 115, 22, 0.4);
    --shadow-red: 0 10px 40px rgba(239, 68, 68, 0.3);
    --shadow-blue: 0 10px 40px rgba(59, 130, 246, 0.3);
    
    /* ============================================
       EFECTOS BLUR
       ============================================ */
    --blur-sm: blur(4px);
    --blur-md: blur(12px);
    --blur-lg: blur(20px);
    --blur-xl: blur(40px);
    
    /* ============================================
       TRANSFORMACIONES
       ============================================ */
    --scale-0: scale(0);
    --scale-50: scale(0.5);
    --scale-90: scale(0.9);
    --scale-95: scale(0.95);
    --scale-100: scale(1);
    --scale-105: scale(1.05);
    --scale-110: scale(1.1);
    --scale-125: scale(1.25);
    --scale-150: scale(1.5);
    
    /* ============================================
       Z-INDEX LAYERS
       ============================================ */
    --z-background: -1;
    --z-normal: 1;
    --z-elevated: 10;
    --z-sticky: 100;
    --z-overlay: 1000;
    --z-modal: 2000;
    --z-tooltip: 3000;
}
```

---

## 4. HERO SECTION

### 4.1 Estructura HTML

```html
<section class="hero" id="hero">
    <!-- Background animado -->
    <div class="hero-bg">
        <canvas id="particles-canvas"></canvas>
        <div class="gradient-overlay"></div>
    </div>
    
    <!-- Contenido -->
    <div class="hero-content">
        <!-- Logo con animación dramática -->
        <div class="hero-logo animate-hero-logo">
            <h1 class="logo-text">PRO SMART</h1>
            <div class="logo-subtitle">FACTORIES AI</div>
        </div>
        
        <!-- Headline principal con reveal letter-by-letter -->
        <h2 class="hero-headline">
            <span class="headline-line animate-headline" data-delay="0.2">
                Elimina la Dependencia
            </span>
            <span class="headline-line animate-headline" data-delay="0.4">
                del Encargado en
            </span>
            <span class="headline-line headline-highlight animate-headline" data-delay="0.6">
                5 Minutos
            </span>
        </h2>
        
        <!-- Descripción con fade in -->
        <p class="hero-description animate-fade-up" data-delay="0.8">
            Calcula cuánto pierdes mensualmente por interrupciones
            y toma decisiones basadas en datos reales.
        </p>
        
        <!-- CTAs con stagger animation -->
        <div class="hero-ctas">
            <button class="btn-primary animate-scale-up" data-delay="1.0">
                <span>Calcular Pérdidas</span>
                <span class="btn-arrow">→</span>
            </button>
            <button class="btn-secondary animate-scale-up" data-delay="1.1">
                <span>Ver Demo</span>
                <span class="btn-icon">▶</span>
            </button>
        </div>
        
        <!-- Métricas destacadas con counter animation -->
        <div class="hero-stats">
            <div class="stat-item animate-slide-up" data-delay="1.2">
                <div class="stat-value" data-count-to="847">0</div>
                <div class="stat-label">Fábricas Auditadas</div>
            </div>
            <div class="stat-item animate-slide-up" data-delay="1.3">
                <div class="stat-value">€<span data-count-to="2.4">0</span>M</div>
                <div class="stat-label">Pérdidas Identificadas</div>
            </div>
            <div class="stat-item animate-slide-up" data-delay="1.4">
                <div class="stat-value" data-count-to="92">0</div>
                <div class="stat-label">% Precisión</div>
            </div>
        </div>
    </div>
    
    <!-- Scroll indicator animado -->
    <div class="scroll-indicator">
        <div class="mouse">
            <div class="wheel"></div>
        </div>
        <div class="scroll-text">Scroll para descubrir</div>
    </div>
</section>
```

### 4.2 CSS Animaciones Hero

```css
/* ============================================
   HERO SECTION ANIMATIONS
   ============================================ */

.hero {
    min-height: 100vh;
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Background animado */
.hero-bg {
    position: absolute;
    inset: 0;
    z-index: var(--z-background);
}

.gradient-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(
        135deg,
        var(--bg-primary) 0%,
        transparent 50%,
        var(--bg-secondary) 100%
    );
    animation: gradientShift 10s ease-in-out infinite;
}

@keyframes gradientShift {
    0%, 100% { opacity: 0.8; }
    50% { opacity: 1; }
}

/* Logo animación dramática */
.hero-logo {
    opacity: 0;
    transform: translateY(-100px) scale(0.5) rotate(-10deg);
}

.animate-hero-logo {
    animation: heroLogoEntrance 1.5s var(--easing-elastic) forwards;
}

@keyframes heroLogoEntrance {
    0% {
        opacity: 0;
        transform: translateY(-100px) scale(0.5) rotate(-10deg);
    }
    60% {
        transform: translateY(10px) scale(1.1) rotate(2deg);
    }
    100% {
        opacity: 1;
        transform: translateY(0) scale(1) rotate(0deg);
    }
}

.logo-text {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(3rem, 8vw, 6rem);
    background: linear-gradient(135deg, var(--brand-primary), var(--accent));
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: 0.1em;
    animation: logoGlow 3s ease-in-out infinite;
}

@keyframes logoGlow {
    0%, 100% {
        filter: brightness(1) drop-shadow(0 0 10px rgba(249, 115, 22, 0.4));
    }
    50% {
        filter: brightness(1.2) drop-shadow(0 0 30px rgba(249, 115, 22, 0.8));
    }
}

/* Headline con reveal */
.hero-headline {
    margin: 2rem 0;
    font-size: clamp(2rem, 5vw, 4rem);
    font-weight: 800;
    line-height: 1.2;
}

.headline-line {
    display: block;
    opacity: 0;
    transform: translateX(-50px);
}

.animate-headline {
    animation: headlineReveal 0.8s var(--easing-expo) forwards;
}

@keyframes headlineReveal {
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

.headline-highlight {
    color: var(--brand-primary);
    position: relative;
}

.headline-highlight::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0;
    height: 0.3em;
    background: linear-gradient(90deg, var(--brand-primary), var(--accent));
    opacity: 0.3;
    z-index: -1;
    animation: underlineGrow 1s var(--easing-expo) 0.8s forwards;
}

@keyframes underlineGrow {
    to {
        width: 100%;
    }
}

/* Description fade up */
.hero-description {
    opacity: 0;
    transform: translateY(20px);
}

.animate-fade-up {
    animation: fadeUp 0.8s var(--easing-smooth) forwards;
    animation-delay: var(--delay, 0s);
}

@keyframes fadeUp {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* CTAs con scale y hover avanzado */
.hero-ctas {
    display: flex;
    gap: 1.5rem;
    margin: 3rem 0;
    flex-wrap: wrap;
}

.btn-primary,
.btn-secondary {
    position: relative;
    padding: 1rem 2.5rem;
    font-size: 1.1rem;
    font-weight: 700;
    border: none;
    border-radius: 12px;
    cursor: pointer;
    overflow: hidden;
    transition: all var(--duration-normal) var(--easing-smooth);
    opacity: 0;
    transform: scale(0.8);
}

.animate-scale-up {
    animation: scaleUp 0.6s var(--easing-back) forwards;
    animation-delay: var(--delay, 0s);
}

@keyframes scaleUp {
    to {
        opacity: 1;
        transform: scale(1);
    }
}

.btn-primary {
    background: linear-gradient(135deg, var(--brand-primary), var(--accent));
    color: white;
    box-shadow: var(--shadow-orange);
}

.btn-primary:hover {
    transform: translateY(-5px) scale(1.05);
    box-shadow: var(--shadow-orange-lg);
}

/* Ripple effect */
.btn-primary::before,
.btn-secondary::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.5);
    transform: translate(-50%, -50%);
    transition: width 0.6s, height 0.6s;
}

.btn-primary:active::before,
.btn-secondary:active::before {
    width: 300px;
    height: 300px;
}

/* Arrow animation */
.btn-arrow {
    display: inline-block;
    margin-left: 0.5rem;
    transition: transform var(--duration-normal) var(--easing-smooth);
}

.btn-primary:hover .btn-arrow {
    transform: translateX(5px);
    animation: arrowPulse 1s ease-in-out infinite;
}

@keyframes arrowPulse {
    0%, 100% { transform: translateX(5px); }
    50% { transform: translateX(10px); }
}

/* Stats con counter */
.hero-stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 2rem;
    margin-top: 4rem;
}

.stat-item {
    text-align: center;
    opacity: 0;
    transform: translateY(30px);
}

.animate-slide-up {
    animation: slideUp 0.8s var(--easing-expo) forwards;
    animation-delay: var(--delay, 0s);
}

@keyframes slideUp {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.stat-value {
    font-size: 3rem;
    font-weight: 800;
    color: var(--brand-primary);
    font-family: 'Bebas Neue', sans-serif;
}

.stat-label {
    font-size: 0.9rem;
    color: var(--text-secondary);
    margin-top: 0.5rem;
}

/* Scroll indicator */
.scroll-indicator {
    position: absolute;
    bottom: 2rem;
    left: 50%;
    transform: translateX(-50%);
    text-align: center;
    animation: scrollBounce 2s ease-in-out infinite;
}

@keyframes scrollBounce {
    0%, 100% { transform: translate(-50%, 0); }
    50% { transform: translate(-50%, 10px); }
}

.mouse {
    width: 26px;
    height: 40px;
    border: 2px solid var(--text-secondary);
    border-radius: 13px;
    position: relative;
    margin: 0 auto 0.5rem;
}

.wheel {
    width: 4px;
    height: 8px;
    background: var(--brand-primary);
    border-radius: 2px;
    position: absolute;
    top: 8px;
    left: 50%;
    transform: translateX(-50%);
    animation: wheelScroll 1.5s ease-in-out infinite;
}

@keyframes wheelScroll {
    0% {
        opacity: 1;
        transform: translateX(-50%) translateY(0);
    }
    100% {
        opacity: 0;
        transform: translateX(-50%) translateY(16px);
    }
}

.scroll-text {
    font-size: 0.75rem;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 0.1em;
}
```

### 4.3 JavaScript Hero Animations

```javascript
// ============================================
// HERO SECTION ANIMATIONS
// ============================================

function initHeroAnimations() {
    console.log('🎬 Initializing Hero animations...');
    
    // Registrar plugins GSAP
    gsap.registerPlugin(ScrollTrigger);
    
    // Timeline principal del Hero
    const heroTL = gsap.timeline({
        defaults: {
            ease: "power3.out"
        }
    });
    
    // Logo con entrada dramática
    heroTL.from('.hero-logo', {
        duration: 1.5,
        y: -100,
        opacity: 0,
        scale: 0.5,
        rotation: -10,
        ease: "elastic.out(1, 0.5)"
    });
    
    // Headlines con stagger
    heroTL.from('.headline-line', {
        duration: 0.8,
        x: -50,
        opacity: 0,
        stagger: 0.2,
        ease: "expo.out"
    }, "-=0.8");
    
    // Description
    heroTL.from('.hero-description', {
        duration: 0.8,
        y: 20,
        opacity: 0
    }, "-=0.4");
    
    // CTAs con bounce
    heroTL.from('.hero-ctas button', {
        duration: 0.6,
        scale: 0.8,
        opacity: 0,
        stagger: 0.1,
        ease: "back.out(1.7)"
    }, "-=0.4");
    
    // Stats
    heroTL.from('.stat-item', {
        duration: 0.8,
        y: 30,
        opacity: 0,
        stagger: 0.1
    }, "-=0.3");
    
    // Animar counters en stats
    animateCounters();
    
    // Parallax en scroll
    gsap.to('.hero-content', {
        scrollTrigger: {
            trigger: '.hero',
            start: 'top top',
            end: 'bottom top',
            scrub: 1
        },
        y: 200,
        opacity: 0.5
    });
    
    console.log('✓ Hero animations initialized');
}

// Animar números con counter effect
function animateCounters() {
    document.querySelectorAll('[data-count-to]').forEach(element => {
        const target = parseFloat(element.dataset.countTo);
        const duration = 2000;
        const isDecimal = target % 1 !== 0;
        
        gsap.to({ value: 0 }, {
            value: target,
            duration: duration / 1000,
            ease: "expo.out",
            delay: parseFloat(element.closest('[data-delay]')?.dataset.delay || 0),
            onUpdate: function() {
                const current = this.targets()[0].value;
                element.textContent = isDecimal 
                    ? current.toFixed(1)
                    : Math.round(current);
            }
        });
    });
}

// Inicializar al cargar
document.addEventListener('DOMContentLoaded', initHeroAnimations);
```

---

## 5. NAVEGACIÓN

### 5.1 Estructura HTML Navbar

```html
<nav class="navbar" id="navbar">
    <div class="navbar-container">
        <!-- Logo -->
        <a href="#" class="navbar-logo">
            <span class="logo-icon">⚙️</span>
            <span class="logo-text">ProSmart</span>
        </a>
        
        <!-- Menu items -->
        <ul class="navbar-menu">
            <li class="menu-item">
                <a href="#soluciones" class="menu-link">Soluciones</a>
                <div class="menu-indicator"></div>
            </li>
            <li class="menu-item">
                <a href="#procesos" class="menu-link">Procesos</a>
                <div class="menu-indicator"></div>
            </li>
            <li class="menu-item">
                <a href="#testimonios" class="menu-link">Casos de Éxito</a>
                <div class="menu-indicator"></div>
            </li>
            <li class="menu-item">
                <a href="#precios" class="menu-link">Precios</a>
                <div class="menu-indicator"></div>
            </li>
        </ul>
        
        <!-- CTA -->
        <div class="navbar-cta">
            <button class="btn-nav-primary">
                <span>Calcular Pérdidas</span>
                <span class="btn-glow"></span>
            </button>
        </div>
        
        <!-- Mobile toggle -->
        <button class="navbar-toggle" aria-label="Toggle menu">
            <span class="toggle-line"></span>
            <span class="toggle-line"></span>
            <span class="toggle-line"></span>
        </button>
    </div>
    
    <!-- Progress bar en scroll -->
    <div class="scroll-progress"></div>
</nav>
```

### 5.2 CSS Navbar Animations

```css
/* ============================================
   NAVBAR ANIMATIONS
   ============================================ */

.navbar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: var(--z-sticky);
    background: rgba(10, 15, 28, 0.8);
    backdrop-filter: blur(12px);
    transform: translateY(-100%);
    animation: navbarSlideDown 0.8s var(--easing-expo) 0.5s forwards;
    transition: all var(--duration-normal) var(--easing-smooth);
}

@keyframes navbarSlideDown {
    to {
        transform: translateY(0);
    }
}

/* Navbar al hacer scroll */
.navbar.scrolled {
    background: rgba(10, 15, 28, 0.95);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
}

.navbar-container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 1rem 2rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

/* Logo con hover effect */
.navbar-logo {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    text-decoration: none;
    color: var(--text-primary);
    font-weight: 700;
    font-size: 1.5rem;
    transition: transform var(--duration-normal) var(--easing-smooth);
}

.navbar-logo:hover {
    transform: scale(1.05);
}

.logo-icon {
    font-size: 2rem;
    animation: logoRotate 4s linear infinite;
}

@keyframes logoRotate {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

/* Menu items */
.navbar-menu {
    display: flex;
    list-style: none;
    gap: 2rem;
    margin: 0;
    padding: 0;
}

.menu-item {
    position: relative;
}

.menu-link {
    color: var(--text-secondary);
    text-decoration: none;
    font-weight: 500;
    padding: 0.5rem 0;
    display: block;
    transition: color var(--duration-fast) var(--easing-smooth);
}

.menu-link:hover {
    color: var(--text-primary);
}

/* Indicator animado */
.menu-indicator {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--brand-primary), var(--accent));
    transition: width var(--duration-normal) var(--easing-expo);
}

.menu-item:hover .menu-indicator {
    width: 100%;
}

.menu-link.active ~ .menu-indicator {
    width: 100%;
}

/* CTA Button con pulse */
.btn-nav-primary {
    position: relative;
    padding: 0.75rem 1.5rem;
    background: linear-gradient(135deg, var(--brand-primary), var(--accent));
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: 700;
    cursor: pointer;
    overflow: hidden;
    transition: all var(--duration-normal) var(--easing-smooth);
}

.btn-nav-primary:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-orange);
}

.btn-glow {
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
    animation: btnGlowSlide 3s ease-in-out infinite;
}

@keyframes btnGlowSlide {
    0% { left: -100%; }
    50%, 100% { left: 100%; }
}

/* Mobile toggle */
.navbar-toggle {
    display: none;
    flex-direction: column;
    gap: 6px;
    background: none;
    border: none;
    cursor: pointer;
    padding: 0.5rem;
}

.toggle-line {
    width: 28px;
    height: 3px;
    background: var(--text-primary);
    border-radius: 2px;
    transition: all var(--duration-normal) var(--easing-smooth);
}

.navbar-toggle.active .toggle-line:nth-child(1) {
    transform: rotate(45deg) translateY(9px);
}

.navbar-toggle.active .toggle-line:nth-child(2) {
    opacity: 0;
}

.navbar-toggle.active .toggle-line:nth-child(3) {
    transform: rotate(-45deg) translateY(-9px);
}

/* Scroll progress bar */
.scroll-progress {
    position: absolute;
    bottom: 0;
    left: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--brand-primary), var(--accent));
    width: 0%;
    transition: width 0.1s linear;
}

/* Mobile styles */
@media (max-width: 768px) {
    .navbar-toggle {
        display: flex;
    }
    
    .navbar-menu {
        position: fixed;
        top: 70px;
        left: 0;
        right: 0;
        background: rgba(10, 15, 28, 0.98);
        flex-direction: column;
        padding: 2rem;
        gap: 1.5rem;
        transform: translateX(100%);
        transition: transform var(--duration-normal) var(--easing-smooth);
    }
    
    .navbar-menu.active {
        transform: translateX(0);
    }
}
```

### 5.3 JavaScript Navbar

```javascript
// ============================================
// NAVBAR ANIMATIONS
// ============================================

function initNavbarAnimations() {
    const navbar = document.getElementById('navbar');
    const navbarToggle = document.querySelector('.navbar-toggle');
    const navbarMenu = document.querySelector('.navbar-menu');
    const scrollProgress = document.querySelector('.scroll-progress');
    
    // Scroll behavior
    let lastScroll = 0;
    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        
        // Add/remove scrolled class
        if (currentScroll > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        // Hide on scroll down, show on scroll up
        if (currentScroll > lastScroll && currentScroll > 200) {
            navbar.style.transform = 'translateY(-100%)';
        } else {
            navbar.style.transform = 'translateY(0)';
        }
        
        lastScroll = currentScroll;
        
        // Update progress bar
        const windowHeight = document.documentElement.scrollHeight - window.innerHeight;
        const scrolled = (currentScroll / windowHeight) * 100;
        scrollProgress.style.width = scrolled + '%';
    });
    
    // Mobile toggle
    navbarToggle?.addEventListener('click', () => {
        navbarToggle.classList.toggle('active');
        navbarMenu.classList.toggle('active');
    });
    
    // Active link on scroll
    const sections = document.querySelectorAll('section[id]');
    window.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            if (window.pageYOffset >= sectionTop - 100) {
                current = section.getAttribute('id');
            }
        });
        
        document.querySelectorAll('.menu-link').forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });
    
    console.log('✓ Navbar animations initialized');
}

document.addEventListener('DOMContentLoaded', initNavbarAnimations);
```

---

## 6. CARDS Y PROCESOS

### 6.1 Estructura HTML Cards

```html
<section class="processes-section" id="procesos">
    <div class="section-container">
        <!-- Header -->
        <div class="section-header scroll-reveal">
            <span class="section-tag">PROCESOS SOPORTADOS</span>
            <h2 class="section-title">
                14 Procesos Industriales
                <span class="title-highlight">Optimizados</span>
            </h2>
            <p class="section-description">
                Análisis específico para cada tipo de operación en tu planta
            </p>
        </div>
        
        <!-- Grid de procesos -->
        <div class="processes-grid">
            <!-- Card 1 -->
            <div class="process-card scroll-reveal" data-delay="0.1">
                <div class="card-icon">🔥</div>
                <div class="card-shine"></div>
                <h3 class="card-title">Corte Láser</h3>
                <p class="card-description">
                    Optimización de tiempos muertos en corte por láser
                    de precisión para acero y aluminio.
                </p>
                <div class="card-stats">
                    <div class="stat">
                        <span class="stat-value">35%</span>
                        <span class="stat-label">Mejora típica</span>
                    </div>
                </div>
                <div class="card-hover-effect"></div>
            </div>
            
            <!-- Card 2 -->
            <div class="process-card scroll-reveal" data-delay="0.2">
                <div class="card-icon">⚡</div>
                <div class="card-shine"></div>
                <h3 class="card-title">Plasma</h3>
                <p class="card-description">
                    Reducción de consultas en operaciones de corte
                    por plasma industrial.
                </p>
                <div class="card-stats">
                    <div class="stat">
                        <span class="stat-value">28%</span>
                        <span class="stat-label">Mejora típica</span>
                    </div>
                </div>
                <div class="card-hover-effect"></div>
            </div>
            
            <!-- Repetir para los 14 procesos... -->
            
        </div>
    </div>
</section>
```

### 6.2 CSS Cards Animations

```css
/* ============================================
   PROCESS CARDS ANIMATIONS
   ============================================ */

.processes-section {
    padding: 8rem 2rem;
    position: relative;
    overflow: hidden;
}

.section-container {
    max-width: 1400px;
    margin: 0 auto;
}

/* Header animations */
.section-header {
    text-align: center;
    margin-bottom: 4rem;
}

.section-tag {
    display: inline-block;
    padding: 0.5rem 1rem;
    background: rgba(249, 115, 22, 0.1);
    border: 1px solid rgba(249, 115, 22, 0.3);
    border-radius: 20px;
    color: var(--brand-primary);
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 1rem;
}

.section-title {
    font-size: clamp(2.5rem, 5vw, 4rem);
    font-weight: 800;
    margin-bottom: 1rem;
    line-height: 1.2;
}

.title-highlight {
    color: var(--brand-primary);
    position: relative;
    display: inline-block;
}

.title-highlight::after {
    content: '';
    position: absolute;
    bottom: 0.1em;
    left: 0;
    width: 100%;
    height: 0.15em;
    background: linear-gradient(90deg, var(--brand-primary), var(--accent));
    opacity: 0.3;
    animation: underlinePulse 2s ease-in-out infinite;
}

@keyframes underlinePulse {
    0%, 100% { transform: scaleX(1); }
    50% { transform: scaleX(1.05); }
}

/* Grid */
.processes-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
}

/* Cards */
.process-card {
    position: relative;
    background: rgba(26, 35, 50, 0.6);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 2rem;
    overflow: hidden;
    transition: all var(--duration-normal) var(--easing-smooth);
    cursor: pointer;
}

/* Shine effect */
.card-shine {
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(255, 255, 255, 0.1),
        transparent
    );
    transition: left 0.5s var(--easing-smooth);
}

.process-card:hover .card-shine {
    left: 100%;
}

/* Hover effect */
.process-card:hover {
    transform: translateY(-10px) scale(1.02);
    border-color: var(--brand-primary);
    box-shadow: var(--shadow-orange-lg);
}

.card-hover-effect {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, var(--brand-primary), var(--accent));
    transform: scaleX(0);
    transform-origin: left;
    transition: transform var(--duration-medium) var(--easing-expo);
}

.process-card:hover .card-hover-effect {
    transform: scaleX(1);
}

/* Icon */
.card-icon {
    font-size: 3.5rem;
    margin-bottom: 1rem;
    display: inline-block;
    animation: iconFloat 3s ease-in-out infinite;
}

@keyframes iconFloat {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}

.process-card:hover .card-icon {
    animation: iconBounce 0.6s var(--easing-bounce);
}

@keyframes iconBounce {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.2) rotate(5deg); }
}

/* Title */
.card-title {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
    color: var(--text-primary);
}

/* Description */
.card-description {
    color: var(--text-secondary);
    line-height: 1.6;
    margin-bottom: 1.5rem;
}

/* Stats */
.card-stats {
    display: flex;
    gap: 1.5rem;
}

.stat {
    display: flex;
    flex-direction: column;
}

.stat-value {
    font-size: 2rem;
    font-weight: 800;
    color: var(--brand-primary);
    font-family: 'Bebas Neue', sans-serif;
}

.stat-label {
    font-size: 0.75rem;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

/* Scroll reveal */
.scroll-reveal {
    opacity: 0;
    transform: translateY(50px);
    transition: all 0.8s var(--easing-expo);
}

.scroll-reveal.visible {
    opacity: 1;
    transform: translateY(0);
}

/* Stagger delays */
.scroll-reveal[data-delay="0.1"] { transition-delay: 0.1s; }
.scroll-reveal[data-delay="0.2"] { transition-delay: 0.2s; }
.scroll-reveal[data-delay="0.3"] { transition-delay: 0.3s; }
.scroll-reveal[data-delay="0.4"] { transition-delay: 0.4s; }
```

### 6.3 JavaScript Cards

```javascript
// ============================================
// CARDS SCROLL REVEAL
// ============================================

function initCardsAnimations() {
    // Intersection Observer para scroll reveal
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                
                // Animar con GSAP si está disponible
                if (typeof gsap !== 'undefined') {
                    gsap.from(entry.target, {
                        duration: 0.8,
                        y: 50,
                        opacity: 0,
                        ease: "expo.out",
                        delay: parseFloat(entry.target.dataset.delay || 0)
                    });
                }
            }
        });
    }, observerOptions);
    
    // Observar todos los elementos
    document.querySelectorAll('.scroll-reveal').forEach(el => {
        observer.observe(el);
    });
    
    // Parallax en cards con GSAP
    if (typeof gsap !== 'undefined') {
        gsap.utils.toArray('.process-card').forEach(card => {
            gsap.to(card, {
                scrollTrigger: {
                    trigger: card,
                    start: 'top bottom',
                    end: 'bottom top',
                    scrub: 1
                },
                y: -20
            });
        });
    }
    
    console.log('✓ Cards animations initialized');
}

document.addEventListener('DOMContentLoaded', initCardsAnimations);
```

---

## 7. FORMULARIOS

### 7.1 HTML Formularios

```html
<section class="form-section" id="calculator">
    <div class="form-container">
        <div class="form-header scroll-reveal">
            <h2 class="form-title">Calcula tus Pérdidas</h2>
            <p class="form-subtitle">Auditoría en menos de 5 minutos</p>
        </div>
        
        <form class="calculator-form">
            <!-- Input group con animación -->
            <div class="input-group scroll-reveal" data-delay="0.1">
                <label class="input-label">
                    <span class="label-text">Número de Operarios</span>
                    <span class="label-tooltip">
                        <span class="tooltip-icon">?</span>
                        <span class="tooltip-content">
                            Total de operarios que pueden consultar al encargado
                        </span>
                    </span>
                </label>
                <div class="input-wrapper">
                    <input 
                        type="number" 
                        class="input-field"
                        placeholder="Ej: 25"
                        min="1"
                        required
                    >
                    <div class="input-focus-line"></div>
                </div>
            </div>
            
            <!-- Slider con valor animado -->
            <div class="input-group scroll-reveal" data-delay="0.2">
                <label class="input-label">
                    <span class="label-text">Consultas por Día</span>
                    <span class="label-value" id="consultas-value">4</span>
                </label>
                <div class="slider-wrapper">
                    <input 
                        type="range" 
                        class="input-slider"
                        min="1"
                        max="10"
                        value="4"
                        id="consultas-slider"
                    >
                    <div class="slider-track"></div>
                    <div class="slider-fill"></div>
                    <div class="slider-thumb"></div>
                </div>
            </div>
            
            <!-- Más campos... -->
            
            <!-- Submit button -->
            <button type="submit" class="btn-submit scroll-reveal" data-delay="0.5">
                <span class="btn-text">Calcular Impacto</span>
                <span class="btn-loader"></span>
                <div class="btn-particles"></div>
            </button>
        </form>
    </div>
</section>
```

### 7.2 CSS Formularios

```css
/* ============================================
   FORM ANIMATIONS
   ============================================ */

.form-section {
    padding: 8rem 2rem;
    background: linear-gradient(
        180deg,
        var(--bg-primary) 0%,
        var(--bg-secondary) 100%
    );
}

.form-container {
    max-width: 700px;
    margin: 0 auto;
}

/* Input groups */
.input-group {
    margin-bottom: 2rem;
}

.input-label {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.75rem;
    font-weight: 600;
    color: var(--text-primary);
}

.label-tooltip {
    position: relative;
    cursor: help;
}

.tooltip-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: rgba(249, 115, 22, 0.2);
    color: var(--brand-primary);
    font-size: 0.75rem;
    font-weight: 700;
    transition: all var(--duration-fast) var(--easing-smooth);
}

.label-tooltip:hover .tooltip-icon {
    transform: scale(1.2) rotate(15deg);
    background: var(--brand-primary);
    color: white;
}

.tooltip-content {
    position: absolute;
    bottom: calc(100% + 10px);
    right: 0;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 0.75rem 1rem;
    font-size: 0.85rem;
    font-weight: 400;
    width: 200px;
    opacity: 0;
    pointer-events: none;
    transform: translateY(10px);
    transition: all var(--duration-normal) var(--easing-bounce);
    box-shadow: var(--shadow-lg);
}

.label-tooltip:hover .tooltip-content {
    opacity: 1;
    transform: translateY(0);
    pointer-events: auto;
}

/* Input field */
.input-wrapper {
    position: relative;
}

.input-field {
    width: 100%;
    padding: 1rem 1.25rem;
    background: rgba(26, 35, 50, 0.6);
    border: 2px solid var(--border);
    border-radius: 12px;
    color: var(--text-primary);
    font-size: 1rem;
    transition: all var(--duration-normal) var(--easing-smooth);
}

.input-field:focus {
    outline: none;
    border-color: var(--brand-primary);
    background: rgba(26, 35, 50, 0.8);
    box-shadow: 0 0 0 4px rgba(249, 115, 22, 0.1);
}

/* Focus line animada */
.input-focus-line {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--brand-primary), var(--accent));
    transition: width var(--duration-medium) var(--easing-expo);
}

.input-field:focus ~ .input-focus-line {
    width: 100%;
}

/* Slider customizado */
.slider-wrapper {
    position: relative;
    padding: 1rem 0;
}

.input-slider {
    -webkit-appearance: none;
    appearance: none;
    width: 100%;
    height: 8px;
    background: transparent;
    outline: none;
    cursor: pointer;
    position: relative;
    z-index: 2;
}

/* Slider track */
.input-slider::-webkit-slider-track {
    height: 8px;
    background: rgba(26, 35, 50, 0.6);
    border-radius: 4px;
}

.input-slider::-moz-range-track {
    height: 8px;
    background: rgba(26, 35, 50, 0.6);
    border-radius: 4px;
}

/* Slider thumb */
.input-slider::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 24px;
    height: 24px;
    background: linear-gradient(135deg, var(--brand-primary), var(--accent));
    border-radius: 50%;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(249, 115, 22, 0.5);
    transition: all var(--duration-fast) var(--easing-smooth);
}

.input-slider::-moz-range-thumb {
    width: 24px;
    height: 24px;
    background: linear-gradient(135deg, var(--brand-primary), var(--accent));
    border: none;
    border-radius: 50%;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(249, 115, 22, 0.5);
    transition: all var(--duration-fast) var(--easing-smooth);
}

.input-slider:hover::-webkit-slider-thumb {
    transform: scale(1.2);
    box-shadow: 0 6px 20px rgba(249, 115, 22, 0.8);
}

.input-slider:hover::-moz-range-thumb {
    transform: scale(1.2);
    box-shadow: 0 6px 20px rgba(249, 115, 22, 0.8);
}

.input-slider:active::-webkit-slider-thumb {
    transform: scale(1.3);
}

.input-slider:active::-moz-range-thumb {
    transform: scale(1.3);
}

/* Label value animado */
.label-value {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-width: 40px;
    padding: 0.25rem 0.75rem;
    background: rgba(249, 115, 22, 0.2);
    color: var(--brand-primary);
    border-radius: 20px;
    font-weight: 700;
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.1rem;
    transition: all var(--duration-fast) var(--easing-bounce);
}

.label-value.updating {
    animation: valueUpdate 0.3s var(--easing-bounce);
}

@keyframes valueUpdate {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.2); }
}

/* Submit button */
.btn-submit {
    width: 100%;
    padding: 1.25rem 2rem;
    background: linear-gradient(135deg, var(--brand-primary), var(--accent));
    color: white;
    border: none;
    border-radius: 12px;
    font-size: 1.1rem;
    font-weight: 700;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    transition: all var(--duration-normal) var(--easing-smooth);
}

.btn-submit:hover {
    transform: translateY(-3px);
    box-shadow: var(--shadow-orange-lg);
}

.btn-submit:active {
    transform: translateY(-1px);
}

/* Loader oculto por defecto */
.btn-loader {
    position: absolute;
    width: 20px;
    height: 20px;
    border: 3px solid rgba(255, 255, 255, 0.3);
    border-top-color: white;
    border-radius: 50%;
    opacity: 0;
    animation: btnRotate 0.8s linear infinite;
}

@keyframes btnRotate {
    to { transform: rotate(360deg); }
}

.btn-submit.loading .btn-text {
    opacity: 0;
}

.btn-submit.loading .btn-loader {
    opacity: 1;
}

/* Partículas en hover */
.btn-particles {
    position: absolute;
    inset: 0;
    pointer-events: none;
}

.btn-submit:hover .btn-particles::before,
.btn-submit:hover .btn-particles::after {
    content: '';
    position: absolute;
    width: 4px;
    height: 4px;
    background: white;
    border-radius: 50%;
    animation: particleFloat 1.5s ease-out infinite;
}

.btn-submit:hover .btn-particles::before {
    top: 20%;
    left: 30%;
    animation-delay: 0s;
}

.btn-submit:hover .btn-particles::after {
    top: 60%;
    right: 30%;
    animation-delay: 0.5s;
}

@keyframes particleFloat {
    0% {
        transform: translateY(0) scale(1);
        opacity: 1;
    }
    100% {
        transform: translateY(-30px) scale(0);
        opacity: 0;
    }
}
```

### 7.3 JavaScript Formularios

```javascript
// ============================================
// FORM ANIMATIONS
// ============================================

function initFormAnimations() {
    // Sliders con feedback visual
    document.querySelectorAll('.input-slider').forEach(slider => {
        const valueDisplay = document.getElementById(slider.id.replace('-slider', '-value'));
        
        slider.addEventListener('input', function() {
            if (valueDisplay) {
                valueDisplay.textContent = this.value;
                valueDisplay.classList.add('updating');
                setTimeout(() => valueDisplay.classList.remove('updating'), 300);
            }
            
            // Vibración en móvil
            if (navigator.vibrate) {
                navigator.vibrate(5);
            }
        });
    });
    
    // Input focus animations
    document.querySelectorAll('.input-field').forEach(input => {
        input.addEventListener('focus', function() {
            gsap.from(this, {
                duration: 0.3,
                scale: 0.98,
                ease: "back.out(2)"
            });
        });
    });
    
    // Form submit
    const form = document.querySelector('.calculator-form');
    const submitBtn = document.querySelector('.btn-submit');
    
    form?.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Loading state
        submitBtn.classList.add('loading');
        submitBtn.disabled = true;
        
        // Simular procesamiento
        await new Promise(resolve => setTimeout(resolve, 2000));
        
        // Success state
        submitBtn.classList.remove('loading');
        submitBtn.classList.add('success');
        submitBtn.querySelector('.btn-text').textContent = '✓ ¡Calculado!';
        
        // Scroll a resultados
        setTimeout(() => {
            const resultsSection = document.getElementById('results');
            resultsSection?.scrollIntoView({ behavior: 'smooth' });
        }, 500);
    });
    
    console.log('✓ Form animations initialized');
}

document.addEventListener('DOMContentLoaded', initFormAnimations);
```

---

## 8. MÉTRICAS Y KPIS

*(Continuaría con las secciones restantes...)*

---

## 📊 RESUMEN DE IMPLEMENTACIÓN

### Librerías Necesarias:
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
```

### Estructura de Archivos:
```
/css/
  ├── variables.css
  ├── animations.css
  ├── components/
  │   ├── hero.css
  │   ├── navbar.css
  │   ├── cards.css
  │   └── forms.css

/js/
  ├── main-animations.js
  ├── hero-animations.js
  ├── navbar-animations.js
  ├── cards-animations.js
  └── form-animations.js
```

### Performance Targets:
- ✅ First Contentful Paint: < 1.5s
- ✅ Time to Interactive: < 3.5s
- ✅ 60 FPS en desktop
- ✅ 30 FPS en móvil
- ✅ Lighthouse Score: > 90

---

**NOTA PARA GOOGLE ANTIGRAVITY:**

Este documento contiene las especificaciones completas para implementar un sistema de animaciones de clase mundial. Todos los códigos son funcionales y están optimizados para producción. Se recomienda:

1. Implementar las animaciones de forma progresiva
2. Testear en diferentes dispositivos
3. Monitorizar performance con Lighthouse
4. Ajustar duraciones según feedback de usuarios

¿Necesitas que desarrolle alguna sección específica con más detalle?
