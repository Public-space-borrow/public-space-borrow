// 開始時間和結束時間的小時數
const startHour = 8;
const endHour = 24;

// 取得 tbody 元素
const tbody = document.querySelector('tbody');

// 取得第一行的內容
const firstRow = tbody.querySelector('tr:first-child');

// 建立時間行並填入時間
for (let hour = startHour; hour <= endHour; hour++) {
    const newRow = document.createElement('tr'); // 建立新的 <tr> 元素

    // 第一個格子放置時間
    const timeCell = document.createElement('td');
    timeCell.textContent = `${hour}:00`;
    newRow.appendChild(timeCell);

    // 其他格子放置連結，並使用第一行的內容
    firstRow.querySelectorAll('td:not(:first-child)').forEach((cell) => {
        const dataCell = document.createElement('td');
        dataCell.innerHTML = cell.innerHTML; // 複製內容
        newRow.appendChild(dataCell);
    });

    // 將最後一個格子內容設定為時間
    const lastCell = newRow.lastElementChild;
    lastCell.textContent = `${hour}:00`;

    tbody.appendChild(newRow); // 將新的行添加到 tbody 中
}

// 取得表單和彈出框元素
const formPopup = document.getElementById('myForm');
const formContainer = document.querySelector('.form-container');

// 取得所有的觸發連結
const openFormLinks = document.querySelectorAll('.stretched-link');

// 監聽觸發連結的點擊事件
openFormLinks.forEach((link) => {
    link.addEventListener('click', (event) => {
        event.preventDefault(); // 阻止默認的連結行為
        formPopup.style.display = 'block'; // 顯示表單彈出框
    });
});

// 點擊表單彈出框外的區域，關閉表單彈出框
window.addEventListener('click', (event) => {
    if (event.target === formPopup) {
        formPopup.style.display = 'none'; // 隱藏表單彈出框
    }
});












