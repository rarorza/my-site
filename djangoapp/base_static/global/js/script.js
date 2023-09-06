function menuMobile() {
  const mobileMenu = document.querySelector(".fa-bars");
  const navMenu = document.querySelector('header .primary-navigation')

  mobileMenu.addEventListener('click', () => {
    mobileMenu.classList.toggle('fa-x')
    navMenu.classList.toggle('activated')
  })
}

function typingTitle() {
  const title = document.querySelector(".typing");

  function char(element) {
    const arrayTitulo = element.innerHTML.split('');
    element.innerHTML = '';
    arrayTitulo.forEach((letra, i) => {
      setTimeout(() => {
        element.innerHTML += letra;
      }, 75 * i)
    })
  }
  char(title);
}

function aboutMe() {
  const divExperience = document.querySelectorAll('.experience_content div');
  const liExperience = document.querySelectorAll('.experience_content ul li');
  const divEducation = document.querySelectorAll('.education_content div');
  const liEducation = document.querySelectorAll('.education_content ul li');

  divExperience[0].classList.add('activated');
  liExperience[0].classList.add('activated');
  divEducation[0].classList.add('activated');
  liEducation[0].classList.add('activated');

  function slideShowExp(index) {
    divExperience.forEach((div) => {
      div.classList.remove('activated');
    });
    liExperience.forEach((button) => {
      button.classList.remove('activated');
    });
    divExperience[index].classList.add('activated');
    liExperience[index].classList.add('activated');
  }

  function slideShowEdu(index) {
    divEducation.forEach((div) => {
      div.classList.remove('activated');
    });
    liEducation.forEach((button) => {
      button.classList.remove('activated');
    });
    divEducation[index].classList.add('activated');
    liEducation[index].classList.add('activated');
  }

  liExperience.forEach((event, index) => {
    event.addEventListener('click', () => {
      slideShowExp(index);
    });
  });

  liEducation.forEach((event, index) => {
    event.addEventListener('click', () => {
      slideShowEdu(index);
    });
  });
}

function gridProjects(){
  const listAll = document.querySelectorAll('.projects_storage ul li');
  const buttonGeneral = document.querySelectorAll('.projects_models ul li');
  const buttonAll = document.querySelectorAll('.projects_models .all');
  
  function removeClick(index) {
    buttonGeneral.forEach((item) => {
      item.classList.remove('activated');
    });
    buttonGeneral[index].classList.add('activated');
  }

  showLista(listAll);
  
  buttonGeneral.forEach((event, index) => {
    event.addEventListener('click', () => {
      removeClick(index);
    });
  });
  
  buttonGeneral.forEach((item) => {
    item.addEventListener('click', (e) => {
      let currentButton = e.target;
      if (currentButton.classList.contains('all')) {
        showLista(listAll);
      }
      if (currentButton.classList.contains('backend')) {
        showLista(listAll, "backend");
      }
      if (currentButton.classList.contains('data')) {
        showLista(listAll, "data");
      }
      if (currentButton.classList.contains('ia')) {
        showLista(listAll, "ia");
      }
      if (currentButton.classList.contains('all')) {
        showLista(listAll, "all");
      }
    });
  });
  
  function showLista(list, button = "all") {
  
    list.forEach((item) => {
      item.classList.remove('activated');
    })
    if (button == 'backend') {
      list[0].classList.add('activated');
      list[1].classList.add('activated');
      list[2].classList.add('activated');
      list[3].classList.add('activated');
    }
    if (button == 'data') {
      list[4].classList.add('activated');
      list[5].classList.add('activated');
    }
    if (button == 'ia') {
      list[6].classList.add('activated');
      list[7].classList.add('activated');
    }
    if (button == 'all') {
      for (let i = 0; i < list.length; i++) {
        list[i].classList.add('activated');
      }
    }
  }
}

gridProjects();
typingTitle();
menuMobile();
aboutMe();
