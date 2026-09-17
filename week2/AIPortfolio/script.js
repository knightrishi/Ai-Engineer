
const modals = {
  parabit: {
    label: 'Desktop · Enterprise · Transportation',
    title: 'ParabitINSS',
    tagline: 'Intelligent toll and vehicle monitoring system',
    challenge: 'Design a desktop application that handles real-time vehicle data ingestion, analytics dashboards, and toll management - without a backend server.',
    solution: 'Built a Java desktop application with JavaFX for rich UI, Swing components for legacy compatibility, JDBC for direct MySQL access, and real-time graph rendering for analytics.',
    arch: [
      'Java backend architecture with JDBC integration',
      'Real-time graph updates and dashboard rendering',
      'Vehicle analytics and scalable monitoring design',
      'Intelligent toll management and data visualization',
      'MySQL persistence with optimized query design'
    ],
    tech: ['Java', 'JavaFX', 'Swing', 'MySQL', 'JDBC'],
    github: "https://github.com/knightrishi/ParabitINSS"
  },
  lifeline: {
    label: 'Full-Stack · Production · Healthcare',
    title: 'LifeLine',
    tagline: 'Blood donation management that connects donors, hospitals, and recipients',
    challenge: 'Coordinate a three-party system (donors, hospitals, recipients) with real-time blood inventory, smart matching by type and location, and a clean user experience under urgency.',
    solution: 'Full-stack MERN application with a RESTful Node.js API, MongoDB for flexible donor/hospital schemas, Express middleware for auth, and a React frontend optimized for speed.',
    arch: [
      'Node.js backend with MongoDB and Express.js',
      'Real-time blood inventory and availability tracking',
      'Tri-party coordination system (donor/hospital/recipient)',
      'Smart donor matching by blood type and location',
      'RESTful API architecture for scalable integration'
    ],
    tech: ['React', 'Node.js', 'Express.js', 'MongoDB', 'JWT'],
    github: 'https://github.com/knightrishi/LifeLine'
  },
  darshan: {
    label: 'Full-Stack · Production · Travel',
    title: 'Darshan Ease',
    tagline: 'Temple darshan booking and management platform',
    challenge: 'Build a full-stack booking platform for temple visits with admin dashboards, scheduling, authentication flows, and a seamless user-facing booking experience.',
    solution: 'React + Node.js application with an Express API layer, MongoDB persistence, and role-based authentication for admin vs. visitor workflows. Booking slots managed server-side with conflict prevention.',
    arch: [
      'Booking management with admin dashboard',
      'Role-based authentication (admin vs. visitor)',
      'Scalable scheduling system with conflict detection',
      'Full-stack React + Node.js integration',
      'MongoDB schemas for temple, slot, and booking data'
    ],
    tech: ['React', 'Node.js', 'Express.js', 'MongoDB'],
    github: 'https://github.com/knightrishi/Darshan-Ease'
  },
  travelers: {
    label: 'Frontend · MVP · Travel',
    title: 'Travelers',
    tagline: 'Immersive travel discovery and destination platform',
    challenge: 'Create a visually compelling travel platform that communicates destination stories through design - immersive UI, smooth animations, and a fully responsive layout.',
    solution: 'React.js with custom CSS animations, component-driven architecture, and responsive design from mobile to desktop. Focused on UI craft and storytelling through visual hierarchy.',
    arch: [
      'Interactive UI with immersive scroll animations',
      'Destination management component system',
      'Fully responsive across mobile, tablet, desktop',
      'Frontend-focused React component architecture',
      'CSS3 custom transitions and motion design'
    ],
    tech: ['React.js', 'JavaScript', 'CSS3', 'HTML5'],
    github: 'https://github.com/knightrishi/Travelers'
  },
  shorturl: {
    label: 'Backend · Production · DevTools',
    title: 'Short URL System',
    tagline: 'Production-grade URL shortening service built for scale',
    challenge: 'Build a backend URL shortening service that handles high-volume redirect traffic, collision-resistant hash generation, and persistent routing with analytics tracking.',
    solution: 'Node.js + Express REST API with MongoDB persistence, hash-based short code generation with collision handling, redirect middleware, and a clean endpoint design for integration.',
    arch: [
      'Hash-based short URL generation with collision detection',
      'Redirect handling with click analytics tracking',
      'RESTful API architecture and MongoDB persistence',
      'Efficient routing and async request handling',
      'Express middleware pipeline for logging and errors'
    ],
    tech: ['Node.js', 'Express.js', 'MongoDB'],
    github: 'https://github.com/knightrishi/Backend-Node/tree/main/Short-URL'
  },
  search: {
    label: 'Backend · Production · DevTools',
    title: 'Distributed Search Engine',
    tagline: 'Search at scale -across distributed nodes, without Elasticsearch',
    challenge: 'Implement a production-grade distributed search engine from scratch in Java and Spring Boot -covering web crawling, tokenization, TF-IDF ranking, consistent hashing for shard coordination, and a scatter-gather query engine. No Lucene. No Elasticsearch.',
    solution: 'Java + Spring Boot distributed system with a BFS web crawler parsing robots.txt, a custom tokenizer and inverted index, TF-IDF scoring from scratch, consistent hashing for shard routing, and a scatter-gather REST API with boolean query support. Deployed via Docker Compose.',
    arch: [
      'BFS web crawler with robots.txt compliance',
      'Tokenizer, stemmer, and inverted index builder',
      'TF-IDF scoring implemented from first principles',
      'Consistent hashing for shard coordination across nodes',
      'Scatter-gather query engine with boolean query support',
      'Spring Boot REST API + Docker Compose deployment'
    ],
    tech: ['Java', 'Spring Boot', 'Distributed Systems', 'TF-IDF', 'Docker'],
    github: 'https://github.com/knightrishi/distributed-search-engine'
  }

};


function openModal(key) {
  const m = modals[key];
  if (!m) return;
  document.getElementById('modal-body').innerHTML = `
    <div class="modal-label">${m.label}</div>
    <h2 class="modal-title">${m.title}</h2>
    <p class="modal-tagline">${m.tagline}</p>
    <div class="modal-split">
      <div>
        <div class="modal-block-title">The Challenge</div>
        <div class="modal-block-body">${m.challenge}</div>
      </div>
      <div>
        <div class="modal-block-title">The Solution</div>
        <div class="modal-block-body">${m.solution}</div>
      </div>
    </div>
    <div class="modal-arch">
      <div class="modal-block-title">Architecture Highlights</div>
      <ul class="arch-list">
        ${m.arch.map(a => `<li>${a}</li>`).join('')}
      </ul>
    </div>
    <div class="modal-block-title" style="margin-bottom:0.75rem;">Tech Stack</div>
    <div class="modal-tech-row">
      ${m.tech.map(t => `<span class="modal-tech-tag">${t}</span>`).join('')}
    </div>
    <div class="modal-actions">
      <a class="btn-primary" href="${m.github}" target="_blank" style="font-size:0.85rem;padding:0.7rem 1.4rem;">View on GitHub ↗</a>
      <a class="btn-secondary" href="#contact" onclick="closeModal()" style="font-size:0.85rem;padding:0.7rem 1.4rem;">Start similar project</a>
    </div>
  `;
  document.getElementById('modal-overlay').classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeModal(e) {
  if (e && e.target !== document.getElementById('modal-overlay') && e.type !== 'click') return;
  if (e && e.currentTarget === document.getElementById('modal-content')) return;
  document.getElementById('modal-overlay').classList.remove('open');
  document.body.style.overflow = '';
}

// ================= INITIALIZE PORTFOLIO =================

document.addEventListener("DOMContentLoaded", () => {

  // ---------- Project Cards ----------

  document.querySelectorAll(".project-card").forEach((card) => {
    card.addEventListener("click", (e) => {
      if (e.target.closest(".card-link")) return;
      openModal(card.dataset.modal);
    });
  });

  // ---------- Modal ----------

  const modalOverlay = document.getElementById("modal-overlay");
  const modalContent = document.getElementById("modal-content");

  if (modalOverlay) {
    modalOverlay.addEventListener("click", closeModal);
  }

  if (modalContent) {
    modalContent.addEventListener("click", (e) => e.stopPropagation());
  }

  // ---------- Filters ----------

  const activeFilters = {
    type: "all",
    industry: "all",
    scale: "all",
  };

  document.querySelectorAll(".filter-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      const filter = btn.dataset.filter;
      const value = btn.dataset.val;

      activeFilters[filter] = value;

      document
        .querySelectorAll(`.filter-btn[data-filter="${filter}"]`)
        .forEach((b) => b.classList.remove("active"));

      btn.classList.add("active");

      let count = 0;

      document.querySelectorAll(".project-card").forEach((card) => {
        const match =
          (activeFilters.type === "all" ||
            card.dataset.type === activeFilters.type) &&
          (activeFilters.industry === "all" ||
            card.dataset.industry === activeFilters.industry) &&
          (activeFilters.scale === "all" ||
            card.dataset.scale === activeFilters.scale);

        card.style.display = match ? "" : "none";

        if (match) count++;
      });

      const showingCount = document.getElementById("showing-count");
      if (showingCount) showingCount.textContent = count;
    });
  });

  // ---------- AI CHAT ----------

  const chatButton = document.getElementById("chat-button");
  const chatBox = document.getElementById("chat-box");
  const chatMessages = document.getElementById("chat-messages");
  const chatInput = document.getElementById("chat-question");
  const sendButton = document.getElementById("send-chat");

  if (
    chatButton &&
    chatBox &&
    chatMessages &&
    chatInput &&
    sendButton
  ) {
    chatButton.addEventListener("click", () => {
      chatBox.classList.toggle("open");
    });

    async function askAI() {
      const question = chatInput.value.trim();
      if (!question) return;

      chatMessages.innerHTML += `
        <div class="user-msg">${question}</div>
      `;

      chatInput.value = "";

      const loading = document.createElement("div");
      loading.className = "bot-msg loading";
      loading.textContent = "Thinking...";
      chatMessages.appendChild(loading);

      chatMessages.scrollTop = chatMessages.scrollHeight;
      const API_URL = "https://ai-portfolio-backend-fl2t.onrender.com/ask";
      try {
        const response = await fetch(API_URL, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ question }),
        });

        const data = await response.json();

        loading.remove();

        chatMessages.innerHTML += `
          <div class="bot-msg">${data.answer}</div>
        `;
      } catch (err) {
        console.error(err);

        loading.remove();

        chatMessages.innerHTML += `
          <div class="bot-msg error">
            Unable to connect to AI backend.
          </div>
        `;
      }

      chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    sendButton.addEventListener("click", askAI);

    chatInput.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        e.preventDefault();
        askAI();
      }
    });
  } else {
    console.warn("AI chat widget not found in HTML.");
  }
});