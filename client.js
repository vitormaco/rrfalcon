const url = 'http://192.168.0.107:5000/';

console.log('url', url);

let carSpeed = 0;
let carDirection = 0;
let keyPressed = {
  UP: false,
  DOWN: false,
  LEFT: false,
  RIGHT: false,
  Q: false
}

const arrowsElements = {
  UP: null,
  DOWN: null,
  LEFT: null,
  RIGHT: null
}

let speedElement;

const configArrows = () => {
  arrowsElements.UP = document.getElementById('arrow-up');
  arrowsElements.DOWN = document.getElementById('arrow-down');
  arrowsElements.LEFT = document.getElementById('arrow-left');
  arrowsElements.RIGHT = document.getElementById('arrow-right');
}

const getGasData = () => {
}

const getTempHumData = () => {
}

const moveCar = (command) => {
  const options = {
    method: 'POST',
    body: JSON.stringify(command),
    headers: {
        'Content-Type': 'application/json'
    }
  }
  console.log('making move request', command);
  fetch(url + 'move', options).then(res => {
    res.text().then(data => {
    });
  }).catch(err => {
  })
}

const turnCar = (command) => {
  const options = {
    method: 'POST',
    body: JSON.stringify(command),
    headers: {
        'Content-Type': 'application/json'
    }
  }
  console.log('url', url);
  fetch(url + 'turn', options).then(res => {
    res.text().then(data => {
    });
  }).catch(err => {
  })
}

const turnCamera = (command) => {
}

const updateSpeed = () => {
  console.log('updating speed', carSpeed);
  const vel = carSpeed/25;
  speedElement.innerText = vel + '';
}

const arrowLeft = (down) => {
  if (down) {
    keyPressed.LEFT = true;
    arrowsElements.LEFT.classList.add('arrow-selected');
    carDirection = -100;
    turnCar({
      degrees: carDirection
    });
  } else {
    keyPressed.LEFT = false;
    arrowsElements.LEFT.classList.remove('arrow-selected');
    carDirection = 0;
    turnCar({
      degrees: carDirection
    });
  }
}

const arrowRight = (down) => {
  if (down) {
    keyPressed.RIGHT = true;
    arrowsElements.RIGHT.classList.add('arrow-selected');
    carDirection = 100;
    turnCar({
      degrees: carDirection
    });
  } else {
    keyPressed.RIGHT = false;
    arrowsElements.RIGHT.classList.remove('arrow-selected');
    carDirection = 0;
    turnCar({
      degrees: carDirection
    });
  }
}

const arrowUp = (down) => {
  if (down) {
    keyPressed.UP = true;
    arrowsElements.UP.classList.add('arrow-selected');
    carSpeed = 50;
    moveCar({
      speed: carSpeed
    });
    updateSpeed();
  } else {
    keyPressed.UP = false;
    arrowsElements.UP.classList.remove('arrow-selected');
    carSpeed = 0;
    moveCar({
      speed: carSpeed
    });
    updateSpeed();
  }
}

const arrowDown = (down) => {
  if (down) {
    keyPressed.DOWN = true;
    arrowsElements.DOWN.classList.add('arrow-selected');
    carSpeed = -50;
    moveCar({
      speed: carSpeed
    });
    updateSpeed();
  } else {
    keyPressed.DOWN = false;
    arrowsElements.DOWN.classList.remove('arrow-selected');
    carSpeed = 0;
    moveCar({
      speed: carSpeed
    });
    updateSpeed();
  }
}

const QKey = () => {
  console.log('q key');
  keyPressed.Q = true;
  if (keyPressed.UP && carSpeed < 100) {
    carSpeed += 25;
    moveCar({
      speed: carSpeed
    });
    updateSpeed();
  } else if (keyPressed.DOWN && carSpeed > -100) {
    carSpeed -= 25;
    moveCar({
      speed: carSpeed
    });
    updateSpeed();
  }
}

const keyDown = (event) => {
  console.log(event);
  switch(event.code) {
    case ("ArrowLeft"):
      if (!keyPressed.LEFT)
        arrowLeft(true);
      break;
    case ("ArrowRight"):
      if (!keyPressed.RIGHT)
        arrowRight(true);
      break;
    case ("ArrowUp"):
      if (!keyPressed.UP)
        arrowUp(true);
      break;
    case ("ArrowDown"):
      if (!keyPressed.DOWN)
        arrowDown(true);
      break;
    case ("KeyQ"):
      if (!keyPressed.Q)
        QKey();
      break;
  }
}

const keyUp = (event) => {
  switch(event.code) {
    case ("ArrowLeft"):
      arrowLeft(false);
      break;
    case ("ArrowRight"):
      arrowRight(false);
      break;
    case ("ArrowUp"):
      arrowUp(false);
      break;
    case ("ArrowDown"):
      arrowDown(false);
      break;
    case ("KeyQ"):
        keyPressed.Q = false;
        break;
  }
}

const init = () => {
  console.log('init');
  configArrows();
  speedElement = document.getElementById('speed-field');
}

window.onkeydown = keyDown;
window.onkeyup = keyUp;
window.onload = init;