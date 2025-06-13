let gameStarted = false;
let reactionTime = null;
const screenEl = document.getElementById('screen');

// Начало игры
function startGame() {
    document.querySelector('.menu').classList.add('hidden');
    document.querySelector('.game').classList.remove('hidden');
    setTimeout(changeScreen, Math.random() * 3000 + 1000); // задержка до появления зеленого цвета
}

// Изменение цвета экрана на зеленый и начало замера реакции
function changeScreen() {
    screenEl.classList.remove('red-screen');
    screenEl.classList.add('green-screen');
    gameStarted = true;
    reactionTime = Date.now();
}

// Обработка кликов по экрану
screenEl.addEventListener('click', handleClick);

function handleClick() {
    // alert('Клик зарегистрирован!');

    if (!gameStarted || !screenEl.classList.contains('green-screen')) return;

    // Замер результата
    const currentTime = Date.now();
    const resultInMs = currentTime - reactionTime;

    // Отправляем результат обратно в Telegram
    const tg = window.Telegram.WebApp;
    tg.sendData(JSON.stringify({ reaction_time: resultInMs }));
    tg.close(); // Закрытие окна игры

    // Сбрасываем состояние игры для новой попытки
    gameStarted = false;
    screenEl.classList.remove('green-screen');
    screenEl.classList.add('red-screen');
}

// Для дебага добавим обработчик загрузки документа
window.onload = function() {
    console.log('Документ загружен.');
};