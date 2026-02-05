/**
 * PROSMART FACTORIES - PREMIUM 3D ENGINE
 * Skill: 3d-web-experience
 * Pattern: Scroll-Driven 3D Neural Network
 */

let scene, camera, renderer, particles, particleSystem;
let mouseX = 0, mouseY = 0;
let windowHalfX = window.innerWidth / 2;
let windowHalfY = window.innerHeight / 2;

function init3D() {
    const container = document.getElementById('three-canvas-container');
    if (!container) return;

    // 1. Scene Setup
    scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x050505, 0.002);

    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 1, 10000);
    camera.position.z = 1000;

    // 2. Geometry - Neural Particles
    const geometry = new THREE.BufferGeometry();
    const vertices = [];
    const particleCount = 2000;

    for (let i = 0; i < particleCount; i++) {
        vertices.push(
            Math.random() * 2000 - 1000,
            Math.random() * 2000 - 1000,
            Math.random() * 2000 - 1000
        );
    }

    geometry.setAttribute('position', new THREE.Float32BufferAttribute(vertices, 3));

    // 3. Material - Tech Orange
    const material = new THREE.PointsMaterial({
        size: 3,
        color: 0xFF6B00,
        transparent: true,
        opacity: 0.8,
        blending: THREE.AdditiveBlending
    });

    particleSystem = new THREE.Points(geometry, material);
    scene.add(particleSystem);

    // 4. Renderer
    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.setSize(window.innerWidth, window.innerHeight);
    container.appendChild(renderer.domElement);

    // 5. Events
    document.addEventListener('mousemove', onDocumentMouseMove);
    window.addEventListener('resize', onWindowResize);
    window.addEventListener('scroll', onWindowScroll);

    animate();
}

function onWindowResize() {
    windowHalfX = window.innerWidth / 2;
    windowHalfY = window.innerHeight / 2;
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

function onDocumentMouseMove(event) {
    mouseX = (event.clientX - windowHalfX) * 0.1;
    mouseY = (event.clientY - windowHalfY) * 0.1;
}

function onWindowScroll() {
    const scrollPos = window.pageYOffset;
    particleSystem.rotation.y = scrollPos * 0.0005;
    particleSystem.position.z = scrollPos * 0.5;
}

function animate() {
    requestAnimationFrame(animate);
    render();
}

function render() {
    const time = Date.now() * 0.00005;

    camera.position.x += (mouseX - camera.position.x) * 0.05;
    camera.position.y += (-mouseY - camera.position.y) * 0.05;
    camera.lookAt(scene.position);

    particleSystem.rotation.x = time * 0.2;
    particleSystem.rotation.z = time * 0.1;

    renderer.render(scene, camera);
}

// Global Init fallback
document.addEventListener('DOMContentLoaded', () => {
    if (typeof THREE !== 'undefined') {
        init3D();
    } else {
        console.warn('Three.js not loaded. Retrying in 1s...');
        setTimeout(() => {
            if (typeof THREE !== 'undefined') init3D();
        }, 1000);
    }
});
