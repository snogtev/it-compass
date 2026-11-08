//элементы html
const mapArea   = document.querySelector('.map-area');
const popup     = document.getElementById('popup');
const popupName = document.getElementById('popup-name');
const popupInfo = document.getElementById('popup-info');

//размеры viewport окна
const width  = 1000;
const height = 700;

//тэг динамической svg картинки
const svg = d3.select('#map');
//группа для хранения регионов
const g   = svg.append('g'); 

//подгрузка geojson и отрисовка карты(вайбкод)
d3.json('../data/russia_subjects_89.geojson').then(function (data) {
 
    //настройка проекци, сдвиг rotate([-100,0]) чтобы пофиксить чукотку
    const projection = d3.geoConicConformal()
        .rotate([-100, 0])
        .center([0, 62])
        .parallels([52, 68])
        .fitSize([width, height], data); //автоматическая подгонка под размер
 
    //path превращает форму региона в строку для атрибута d тега <path>
    const path = d3.geoPath(projection);
 
    //на каждый регион из файла создаём один <path>
    g.selectAll('path')
        .data(data.features)
        .join('path')
        .attr('d', path)
        .on('click', function (event, d) {
            showPopup(event, d, this);
        });
});

//popup региона(тоже вайбкод)
function showPopup(event, region, pathElement) {
 
    //убираем подсветку с прошлого региона(если) и красим новый
    g.selectAll('path').classed('selected', false);
    d3.select(pathElement).classed('selected', true);
 
    //подставляем данные региона из GeoJSON
    popupName.textContent = region.properties.name;
    popupInfo.textContent = 'Федеральный округ: ' + region.properties.fo;
 
    //координаты клика относительно блока с картой
    const point = d3.pointer(event, mapArea);
 
    //ставим окно у места клика, но не даём ему выйти за края карты
    popup.classList.add('open');       // сначала показываем, иначе высоту не измерить
 
    let left = point[0] + 10;
    let top  = point[1] - popup.offsetHeight - 10;   // окно над курсором
 
    if (top < 10) top = point[1] + 20;                // не влезло сверху - ставим снизу
    if (left + popup.offsetWidth > mapArea.clientWidth) {
        left = mapArea.clientWidth - popup.offsetWidth - 10;
    }
 
    popup.style.left = left + 'px';
    popup.style.top  = top + 'px';
 
    event.stopPropagation();   // чтобы клик не дошёл до карты и не закрыл окно
}

function closePopup() {
    popup.classList.remove('open');
    g.selectAll('path').classed('selected', false);
}

//клик по пустому месту закроет popup
svg.on('click', closePopup);
 
//перемещение по карте
const zoom = d3.zoom()
    .extent([[0, 0], [width, height]])
    .translateExtent([[0, 0], [width, height]])
    .scaleExtent([1, 12])                 //зум от 1x до 12x
    .on('zoom', function (event) {
        g.attr('transform', event.transform);
        closePopup();                     //при движении карты окно закрывается
    });
 
svg.call(zoom);



