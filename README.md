<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>BiddyPhone – Economic Access for the Unbanked</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --primary-orange: #FF6B35;
      --secondary-blue: #2E86AB;
      --accent-purple: #A23B72;
      --dark-bg: #0A0A0A;
      --dark-card: #1A1A1A;
      --light-orange: #F18F01;
      --text-light: #E0E0E0;
      --text-muted: #A0A0A0;
      --success-green: #4ADE80;
      --gradient-primary: linear-gradient(135deg, var(--primary-orange), var(--light-orange));
      --gradient-secondary: linear-gradient(135deg, var(--secondary-blue), var(--accent-purple));
      --gradient-hero: linear-gradient(135deg, var(--dark-bg) 0%, var(--dark-card) 50%, var(--primary-orange) 100%);
    }

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    html {
      scroll-behavior: smooth;
    }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background: var(--dark-bg);
      color: var(--text-light);
      line-height: 1.7;
      overflow-x: hidden;
    }

    /* Navigation */
    nav {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      background: rgba(10, 10, 10, 0.95);
      backdrop-filter: blur(20px);
      z-index: 1000;
      padding: 1rem 2rem;
      border-bottom: 1px solid rgba(255, 107, 53, 0.2);
      transition: all 0.3s ease;
    }

    nav.scrolled {
      background: rgba(10, 10, 10, 0.98);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }

    .nav-container {
      max-width: 1200px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .logo {
      font-size: 1.5rem;
      font-weight: 800;
      background: var(--gradient-primary);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    .nav-links {
      display: flex;
      list-style: none;
      gap: 2rem;
      align-items: center;
    }

    .nav-links a {
      color: var(--text-light);
      text-decoration: none;
      font-weight: 500;
      transition: all 0.3s ease;
      position: relative;
    }

    .nav-links a:hover {
      color: var(--primary-orange);
    }

    .nav-links a::after {
      content: '';
      position: absolute;
      width: 0;
      height: 2px;
      bottom: -5px;
      left: 0;
      background: var(--gradient-primary);
      transition: width 0.3s ease;
    }

    .nav-links a:hover::after {
      width: 100%;
    }

    /* Hero Section */
    #hero {
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      background: var(--gradient-hero);
      position: relative;
      overflow: hidden;
      padding: 2rem;
    }

    #hero::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000"><defs><radialGradient id="a"><stop offset="0%" stop-color="%23FF6B35" stop-opacity="0.1"/><stop offset="100%" stop-color="%23FF6B35" stop-opacity="0"/></radialGradient></defs><circle cx="200" cy="200" r="3" fill="url(%23a)"/><circle cx="800" cy="300" r="2" fill="url(%23a)"/><circle cx="400" cy="600" r="3" fill="url(%23a)"/><circle cx="700" cy="800" r="2" fill="url(%23a)"/></svg>');
      animation: float 20s ease-in-out infinite;
    }

    @keyframes float {
      0%, 100% { transform: translateY(0px) rotate(0deg); }
      50% { transform: translateY(-20px) rotate(180deg); }
    }

    #hero h1 {
      font-size: clamp(3rem, 8vw, 8rem);
      font-weight: 800;
      background: var(--gradient-primary);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      margin-bottom: 1rem;
      position: relative;
      z-index: 2;
      animation: slideInUp 1s ease-out;
    }

    #hero h2 {
      font-size: clamp(1.2rem, 3vw, 2rem);
      color: var(--secondary-blue);
      margin-bottom: 1.5rem;
      font-weight: 600;
      position: relative;
      z-index: 2;
      animation: slideInUp 1s ease-out 0.2s both;
    }

    #hero p {
      font-size: clamp(1rem, 2vw, 1.3rem);
      color: var(--text-muted);
      max-width: 600px;
      margin-bottom: 3rem;
      position: relative;
      z-index: 2;
      animation: slideInUp 1s ease-out 0.4s both;
    }

    .cta-button {
      display: inline-block;
      padding: 1.2rem 3rem;
      background: var(--gradient-primary);
      color: white;
      text-decoration: none;
      border-radius: 50px;
      font-weight: 700;
      font-size: 1.1rem;
      transition: all 0.3s ease;
      position: relative;
      z-index: 2;
      animation: slideInUp 1s ease-out 0.6s both;
      box-shadow: 0 10px 30px rgba(255, 107, 53, 0.3);
    }

    .cta-button:hover {
      transform: translateY(-3px);
      box-shadow: 0 15px 40px rgba(255, 107, 53, 0.4);
    }

    /* Animations */
    @keyframes slideInUp {
      0% {
        opacity: 0;
        transform: translateY(50px);
      }
      100% {
        opacity: 1;
        transform: translateY(0);
      }
    }

    @keyframes fadeIn {
      0% { opacity: 0; }
      100% { opacity: 1; }
    }

    /* Section Styles */
    section {
      padding: 5rem 2rem;
      max-width: 1200px;
      margin: 0 auto;
      position: relative;
    }

    section:not(#hero) {
      opacity: 0;
      transform: translateY(30px);
      transition: all 0.8s ease;
    }

    section.visible {
      opacity: 1;
      transform: translateY(0);
    }

    section h2 {
      font-size: clamp(2rem, 5vw, 3.5rem);
      font-weight: 700;
      margin-bottom: 2rem;
      text-align: center;
      background: var(--gradient-secondary);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    section p {
      font-size: 1.2rem;
      color: var(--text-muted);
      text-align: center;
      max-width: 800px;
      margin: 0 auto 3rem;
    }

    /* Cards and Grid Layouts */
    .problem-grid, .tech-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 2rem;
      margin-top: 3rem;
    }

    .card {
      background: var(--dark-card);
      padding: 2.5rem;
      border-radius: 20px;
      border: 1px solid rgba(255, 107, 53, 0.1);
      transition: all 0.3s ease;
      position: relative;
      overflow: hidden;
    }

    .card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: var(--gradient-primary);
      transform: scaleX(0);
      transition: transform 0.3s ease;
    }

    .card:hover {
      transform: translateY(-5px);
      border-color: rgba(255, 107, 53, 0.3);
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
    }

    .card:hover::before {
      transform: scaleX(1);
    }

    .card h3 {
      color: var(--primary-orange);
      font-size: 1.5rem;
      margin-bottom: 1rem;
      font-weight: 600;
    }

    .card p, .card li {
      color: var(--text-muted);
      line-height: 1.6;
    }

    /* Solution Steps */
    .solution-steps {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 2rem;
      margin-top: 3rem;
    }

    .step {
      background: var(--dark-card);
      padding: 2rem;
      border-radius: 15px;
      text-align: center;
      position: relative;
      border: 2px solid transparent;
      background-clip: padding-box;
    }

    .step::before {
      content: counter(step-counter);
      counter-increment: step-counter;
      position: absolute;
      top: -15px;
      left: 50%;
      transform: translateX(-50%);
      width: 40px;
      height: 40px;
      background: var(--gradient-primary);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      color: white;
      font-size: 1.2rem;
    }

    #solution {
      counter-reset: step-counter;
    }

    /* Tech Stack */
    .tech-item {
      display: flex;
      align-items: flex-start;
      gap: 1rem;
      margin-bottom: 2rem;
    }

    .tech-icon {
      width: 50px;
      height: 50px;
      background: var(--gradient-primary);
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: 1.2rem;
      color: white;
      flex-shrink: 0;
    }

    .tech-content h4 {
      color: var(--primary-orange);
      font-size: 1.3rem;
      margin-bottom: 0.5rem;
    }

    /* Pilot Countries */
    .pilot-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 2rem;
      margin-top: 3rem;
    }

    .pilot-card {
      background: var(--dark-card);
      padding: 2.5rem;
      border-radius: 20px;
      border-left: 5px solid var(--success-green);
      transition: all 0.3s ease;
    }

    .pilot-card:hover {
      transform: translateX(10px);
      box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
    }

    .pilot-card h4 {
      color: var(--success-green);
      font-size: 1.5rem;
      margin-bottom: 1rem;
    }

    /* Statistics */
    .stats {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 2rem;
      margin: 4rem 0;
    }

    .stat {
      text-align: center;
      padding: 2rem;
      background: rgba(255, 107, 53, 0.05);
      border-radius: 15px;
      border: 1px solid rgba(255, 107, 53, 0.1);
    }

    .stat-number {
      font-size: 3rem;
      font-weight: 800;
      color: var(--primary-orange);
      display: block;
      line-height: 1;
    }

    .stat-label {
      color: var(--text-muted);
      margin-top: 0.5rem;
      font-size: 1.1rem;
    }

    /* Join Section */
    #join {
      background: var(--gradient-secondary);
      color: white;
      text-align: center;
      border-radius: 30px;
      margin: 5rem 2rem;
      position: relative;
      overflow: hidden;
    }

    #join::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M 10 0 L 0 0 0 10" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="0.5"/></pattern></defs><rect width="100" height="100" fill="url(%23grid)"/></svg>');
      opacity: 0.3;
    }

    #join h2, #join p {
      position: relative;
      z-index: 2;
    }

    #join h2 {
      color: white;
      background: none;
      -webkit-text-fill-color: white;
    }

    #join p {
      color: rgba(255, 255, 255, 0.9);
    }

    .contact-button {
      display: inline-block;
      padding: 1.2rem 3rem;
      background: white;
      color: var(--secondary-blue);
      text-decoration: none;
      border-radius: 50px;
      font-weight: 700;
      font-size: 1.1rem;
      transition: all 0.3s ease;
      position: relative;
      z-index: 2;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    }

    .contact-button:hover {
      transform: translateY(-3px);
      box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
    }

    /* Mobile Responsiveness */
    @media (max-width: 768px) {
      .nav-links {
        display: none;
      }

      section {
        padding: 3rem 1rem;
      }

      .problem-grid, .tech-grid, .solution-steps, .pilot-grid {
        grid-template-columns: 1fr;
      }

      .stats {
        grid-template-columns: repeat(2, 1fr);
      }

      #join {
        margin: 3rem 1rem;
      }
    }

    /* Scroll Progress Bar */
    .progress-bar {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 3px;
      background: rgba(255, 107, 53, 0.2);
      z-index: 1001;
    }

    .progress-fill {
      height: 100%;
      background: var(--gradient-primary);
      width: 0%;
      transition: width 0.1s ease;
    }

    /* Floating Elements */
    .floating-phone {
      position: fixed;
      bottom: 30px;
      right: 30px;
      width: 60px;
      height: 60px;
      background: var(--gradient-primary);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 10px 30px rgba(255, 107, 53, 0.3);
      transition: all 0.3s ease;
      z-index: 999;
    }

    .floating-phone:hover {
      transform: scale(1.1);
      box-shadow: 0 15px 40px rgba(255, 107, 53, 0.4);
    }

    .floating-phone::before {
      content: '📱';
      font-size: 1.5rem;
    }
  </style>
</head>
<body>
  <!-- Progress Bar -->
  <div class="progress-bar">
    <div class="progress-fill" id="progressFill"></div>
  </div>

  <!-- Navigation -->
  <nav id="navbar">
    <div class="nav-container">
      <div class="logo">BiddyPhone</div>
      <ul class="nav-links">
        <li><a href="#hero">Home</a></li>
        <li><a href="#mission">Mission</a></li>
        <li><a href="#problem">Problem</a></li>
        <li><a href="#solution">Solution</a></li>
        <li><a href="#tech">Technology</a></li>
        <li><a href="#pilots">Pilots</a></li>
        <li><a href="#join">Join</a></li>
      </ul>
    </div>
  </nav>

  <!-- Hero Section -->
  <section id="hero">
    <h1>BiddyPhone</h1>
    <h2>The Bitcoin-Mining Smartphone for the Unbanked</h2>
    <p>Empowering billions with economic sovereignty through solar-powered, off-grid Bitcoin mining.</p>
    <a href="#join" class="cta-button">Join the Movement</a>
  </section>

  <!-- Mission -->
  <section id="mission">
    <h2>Our Mission</h2>
    <p>To democratize access to income and financial tools by turning everyday smartphones into self-powered Bitcoin miners for unbanked populations worldwide.</p>
    
    <div class="stats">
      <div class="stat">
        <span class="stat-number">1.4B</span>
        <div class="stat-label">Adults Unbanked</div>
      </div>
      <div class="stat">
        <span class="stat-number">3B</span>
        <div class="stat-label">Without Internet</div>
      </div>
      <div class="stat">
        <span class="stat-number">100</span>
        <div class="stat-label">Sats Daily UBI</div>
      </div>
      <div class="stat">
        <span class="stat-number">&lt;1W</span>
        <div class="stat-label">Power Consumption</div>
      </div>
    </div>
  </section>

  <!-- Problem Statement -->
  <section id="problem">
    <h2>The Global Challenge</h2>
    <p>Billions of people worldwide are excluded from the global financial system, limiting their economic opportunities and perpetuating cycles of poverty.</p>
    
    <div class="problem-grid">
      <div class="card">
        <h3>Financial Exclusion</h3>
        <p>1.4 billion adults remain unbanked, unable to access basic financial services like savings, loans, or digital payments.</p>
      </div>
      <div class="card">
        <h3>Digital Divide</h3>
        <p>3 billion people lack reliable internet access, cutting them off from digital economic opportunities and services.</p>
      </div>
      <div class="card">
        <h3>Centralized Mining</h3>
        <p>Bitcoin mining is centralized, high-power, and inaccessible to most people, especially those in developing regions.</p>
      </div>
    </div>
  </section>

  <!-- How It Works -->
  <section id="solution">
    <h2>How BiddyPhone Works</h2>
    <p>A revolutionary approach to financial inclusion through distributed Bitcoin mining and solar energy.</p>
    
    <div class="solution-steps">
      <div class="step">
        <h3>Mine Bitcoin Locally</h3>
        <p>Ultra-low-power ASIC chip (&lt;1W) mines Bitcoin efficiently using solar energy.</p>
      </div>
      <div class="step">
        <h3>Solar Power</h3>
        <p>3-5W flexible solar wrap provides sustainable energy for daily operations.</p>
      </div>
      <div class="step">
        <h3>Satellite Sync</h3>
        <p>LEO satellite connectivity with LoRa/BLE mesh network fallback ensures global reach.</p>
      </div>
      <div class="step">
        <h3>Earn Daily UBI</h3>
        <p>Receive ~100 sats daily through built-in DeFi apps and secure wallet integration.</p>
      </div>
    </div>
  </section>

  <!-- Tech Stack -->
  <section id="tech">
    <h2>Revolutionary Technology</h2>
    <p>Advanced hardware and software integration designed for harsh environments and reliable operation.</p>
    
    <div class="tech-grid">
      <div class="card">
        <div class="tech-item">
          <div class="tech-icon">⚡</div>
          <div class="tech-content">
            <h4>ASIC Mining Chip</h4>
            <p>SHA-256 custom chip with &lt;1W power draw, optimized for tropical deployment and continuous operation.</p>
          </div>
        </div>
      </div>
      
      <div class="card">
        <div class="tech-item">
          <div class="tech-icon">☀️</div>
          <div class="tech-content">
            <h4>Solar Power System</h4>
            <p>Flexible solar charging wrap with lithium battery and MPPT controller for maximum efficiency.</p>
          </div>
        </div>
      </div>
      
      <div class="card">
        <div class="tech-item">
          <div class="tech-icon">🛰️</div>
          <div class="tech-content">
            <h4>Satellite Network</h4>
            <p>LEO satellite sync with LoRa mesh fallback and optional GSM for global connectivity.</p>
          </div>
        </div>
      </div>
      
      <div class="card">
        <div class="tech-item">
          <div class="tech-icon">🔒</div>
          <div class="tech-content">
            <h4>BiddyOS Security</h4>
            <p>Hardened Android fork with secure wallet, Bitcoin node, and tamper-proof design.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Pilot Program -->
  <section id="pilots">
    <h2>Global Pilot Programs</h2>
    <p>Strategic deployment in countries with optimal conditions for solar energy, mobile adoption, and regulatory support.</p>
    
    <div class="pilot-grid">
      <div class="pilot-card">
        <h4>🇰🇪 Kenya</h4>
        <p>Strong mobile money ecosystem with M-Pesa integration, high solar exposure, and progressive fintech regulations.</p>
      </div>
      <div class="pilot-card">
        <h4>🇵🇭 Philippines</h4>
        <p>Mesh-friendly archipelago geography with high smartphone usage and strong remittance economy.</p>
      </div>
      <div class="pilot-card">
        <h4>🇬🇭 Ghana</h4>
        <p>Fintech-friendly regulation, cooperative energy infrastructure, and growing crypto adoption.</p>
      </div>
    </div>
  </section>

  <!-- Call to Action -->
  <section id="join">
    <h2>Join the Financial Revolution</h2>
    <p>We're seeking humanitarian partners, crypto-for-good donors, and regional collaborators to bring BiddyPhone to life and empower billions with economic sovereignty.</p>
    <a href="mailto:founders@biddyphone.org" class="contact-button">Contact Our Team</a>
  </section>

  <!-- Floating Action Button -->
  <div class="floating-phone" onclick="scrollToTop()"></div>

  <script>
    // Smooth scrolling and animations
    document.addEventListener('DOMContentLoaded', function() {
      // Intersection Observer for animations
      const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
      };

      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
          }
        });
      }, observerOptions);

      // Observe all sections except hero
      document.querySelectorAll('section:not(#hero)').forEach(section => {
        observer.observe(section);
      });

      // Scroll progress bar
      const progressFill = document.getElementById('progressFill');
      const navbar = document.getElementById('navbar');

      window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const maxHeight = document.documentElement.scrollHeight - window.innerHeight;
        const progress = (scrolled / maxHeight) * 100;
        
        progressFill.style.width = progress + '%';

        // Navbar background change
        if (scrolled > 100) {
          navbar.classList.add('scrolled');
        } else {
          navbar.classList.remove('scrolled');
        }
      });

      // Counter animation for stats
      const animateCounters = () => {
        const counters = document.querySelectorAll('.stat-number');
        counters.forEach(counter => {
          const target = counter.textContent;
          const isNumber = !isNaN(parseFloat(target));
          
          if (isNumber) {
            const targetNum = parseFloat(target);
            const increment = targetNum / 100;
            let current = 0;
            
            const updateCounter = () => {
              if (current < targetNum) {
                current += increment;
                counter.textContent = Math.ceil(current);
                requestAnimationFrame(updateCounter);
              } else {
                counter.textContent = target;
              }
            };
            
            updateCounter();
          }
        });
      };

      // Trigger counter animation when stats section is visible
      const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            animateCounters();
            statsObserver.disconnect();
          }
        });
      });

      const statsSection = document.querySelector('.stats');
      if (statsSection) {
        statsObserver.observe(statsSection);
      }
    });

    // Scroll to top function
    function scrollToTop() {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    }

    // Mobile menu toggle (if needed)
    function toggleMobileMenu() {
      const navLinks = document.querySelector('.nav-links');
      navLinks.classList.toggle('active');
    }

    // Add click tracking for analytics (placeholder)
    document.querySelectorAll('a[href^="#"]').forEach(link => {
      link.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
          target.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
        }
      });
    });

    // Add hover effects for cards
    document.querySelectorAll('.card, .pilot-card').forEach(card => {
      card.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-5px) scale(1.02)';
      });
      
      card.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0) scale(1)';
      });
    });
  </script>
</body>
</html>
# biddyphone-sim
A solar-powered, Bitcoin-native smartphone for off-grid communities.
**BiddyPhone** is an open hardware/software initiative to build a mobile device that can:
- Mine BTC using onboard ASICs
- Sync over mesh and satellite
- Deliver a basic income + communication, off-grid

## 💡 Mission

We aim to empower the unbanked and disconnected with open-source tools for:
- Connectivity
- Sovereignty
- Value transfer

## 🛠️ Current Work

✅ Android Kotlin Simulator (MVP)  
✅ BlockSyncService via LoRa/GSM fallback  
✅ BiddyMiner CPU-mode mining simulation

## 📥 Download

Get the Android simulator APK (or build it yourself).

## 👷 Contribute

We welcome:
- Android developers
- ASIC / FPGA hackers
- Mesh network tinkerers
- Open-source writers & educators

## 🤝 License

Apache 2.0 — Fork, remix, deploy.

---

*Built in public by the BiddyPhone community.*
