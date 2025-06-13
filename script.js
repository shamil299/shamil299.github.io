let gameStarted = false;
let reactionTime = null;
const screenEl = document.getElementById('screen');
const resultEl = document.getElementById('result');
const timeResultEl = document.getElementById('timeResult');

// Начинаем игру
function startGame() {
    document.querySelector('.menu').classList.add('hidden');
    document.querySelector('.game').classList.remove('hidden');
    setTimeout(() => changeScreen(), Math.random() * 3000 + 1000); // задержка до появления зеленого цвета
}

// Меняем цвет экрана на зеленый и начинаем замерять реакцию
function changeScreen() {
    screenEl.classList.remove('red-screen');
    screenEl.classList.add('green-screen');
    gameStarted = true;
    reactionTime = Date.now();
}

// Обработка кликов по экрану
screenEl.addEventListener('click', handleClick);

function handleClick() {
    if (!gameStarted || !screenEl.classList.contains('green-screen')) return;

    // Подсчет результата
    const currentTime = Date.now();
    const resultInMs = currentTime - reactionTime;
    timeResultEl.textContent = resultInMs.toFixed(0);

    // Показываем результат
    screenEl.classList.remove('green-screen');
    screenEl.classList.add('red-screen');
    resultEl.classList.remove('hidden');

    // Готовимся к следующему раунду
    gameStarted = false;
    setTimeout(() => resetGame(), 2000); // пауза между раундами
}

// Перезагрузка игры
function resetGame() {
    resultEl.classList.add('hidden');
    setTimeout(() => changeScreen(), Math.random() * 3000 + 1000); // повторная задержка
}
