<script setup>
import ProjectCard from '@/components/ProjectCard.vue'
import ExperienceCard from '@/components/ExperienceCard.vue'
import { onMounted } from 'vue'
import axios from 'axios'

function getIndex() {
  axios.get('/api/index/').then(response => {
    console.log('index', response.data)
  }).catch(error => {
    console.log('error', error)
  })
}

function mobile() {
  const mobileMenu = document.querySelector(".fa-bars");
  const navMenu = document.querySelector('header .primary-navigation')

  mobileMenu.addEventListener('click', () => {
    mobileMenu.classList.toggle('fa-x')
    navMenu.classList.toggle('activated')
  })
}

function typingTitle() {
  const title = document.querySelector(".typing")

  function chars(element) {
    const titleArray = element.innerHTML.split('')
    element.innerHTML = ''
    titleArray.forEach((char, i) => {
      setTimeout(() => {
        element.innerHTML += char
      }, 75 * i)
    })
  }
  chars(title);
}

onMounted(() => {
  mobile()
  typingTitle()
  getIndex()
})
</script>

<template>
  <main>
    <section aria-label="Section, resume download and social links" class="selection-div" id="home">
      <div>
        <h2>Hello! I am</h2>
        <h2 class="typing">Full Stack Developer</h2>
        <div class="links">
          <a href="#" download="Rafael_Rosa_CV">
            <i class="fa-solid fa-file-arrow-down"></i>CV
          </a>
          <a href="https://br.linkedin.com/in/rarorza" target="_blank" rel="noreferrer">
            <i class="fa-brands fa-linkedin-in"></i>LinkedIn
          </a>
          <a href="https://github.com/rarorza" target="_blank" rel="noreferrer">
            <i class="fa-brands fa-github"></i>GitHub
          </a>
        </div>
      </div>
      <img src="@/assets/imgs/banner.png" alt="Illustrative image of a man's face" />
    </section>

    <section>
      <article aria-label="About me section" class="about-me" id="about-me">
        <div class="about_me_title">
          <h2>About me</h2>
          <p>Professional profile</p>
          <div aria-label="Buttons illustrations section">
            <span></span>
          </div>
        </div>
        <img src="@/assets/imgs/self.png" alt="Image of an illustrative person">
        <div class="about_me_content">
          <div class="about_me_text">
            <h1>I am Rafael</h1>
            <p>
              I have a degree in Law and I'm currently studying Software Analysis and Development. My expertise lies in back-end development, although I also have some knowledge of front-end.
              <br>
              <br>
              I have experience in support, and I currently work as a freelance on some projects.
              <br>
              <br>
              I recently started a blog to discuss various topics (technology, games, movies, etc.) and practice my English. Feel free to engage and send me an email :)
            </p>
          </div>
          <div class="sobre_info">
            <p>
              <i class="fa-sharp fa-solid fa-laptop-code"></i>
              Code: Python [Django, Flask and Selenium], JavaScript
            </p>
            <p>
              <i class="fa-solid fa-location-dot"></i>
              From: São Paulo, Brazil
            </p>
            <p>
              <i class="fa-sharp fa-solid fa-globe"></i>
              Languages: Portuguese and English
            </p>
            <p><i class="fa-solid fa-envelope"></i>
              Email: rarorza@proton.me
            </p>
          </div>
        </div>
      </article>
    </section>

    <section class="projects" id="projects">
      <div class="my_resume" id="resume">
        <div class="about_me_title">
          <h2>Resume</h2>
          <p>A brief summary of my professional and academic experiences</p>
          <div aria-label="Buttons illustrations section">
            <span></span>
          </div>
        </div>
        <div class="resume_general">
          <h2 class="experience">CAREER</h2>
          <ExperienceCard :educationOrJob="`education_content`" />
          <h2 class="education">EDUCATION</h2>
          <ExperienceCard :educationOrJob="`experience_content`" />
        </div>
      </div>
      <div class="about_me_title">
        <h2>Projects</h2>
        <p>My projects</p>
        <div aria-label="Project grid section">
          <span></span>
        </div>
      </div>
      <div class="projects_storage">
        <ul>
          <ProjectCard />
          <ProjectCard />
          <ProjectCard />
        </ul>
      </div>
    </section>
  </main>
</template>
