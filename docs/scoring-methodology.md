# IT Compass — Методология скоринга

## Общая информация

* **Автор документа:** Степан Ногтев
* **Связанные документы:**
  * [`GLOSSARY.md`](./GLOSSARY.md) — глоссарий
  * [`spec.md`](./spec.md) — спецификация

## Назначение

Документ фиксирует три ключевых решения, от которых зависит итоговый рейтинг регионов:

1. **Какие метрики** участвуют в расчёте рейтинга регионов.
2. **Как нормализуются** сырые записи метрик для приведения к единой шкале.
3. **Какие веса** получает каждая метрика для каждого грейда.

На основе этих решений составляется тоговый рейтинг регионов.

## Отбор метрик

### Классификация метрик

Метрики проекта разделены по категориям:

| Категория | Назначение |
| :-------- | :--------- |
| **Экономические** | Насколько выгодно жить и работать |
| **Рыночно-трудовые** | Насколько легко найти работу и сменить её |
| **Образовательные** | Насколько доступно профильное образование |
| **Инфраструктурные** | Насколько развита и современна инфраструктура |
| **Климатическо-экологические** | Насколько благоприятна среда для здоровья |
| **Социально-демографические** | Насколько безопасна и благополучна социальная среда |

### Метрики по категориям

| Категория | Метрика | Направление | Разбивка по грейдам | Источник данных |
| :-------- | :------ | :---------- | :------------------ | :-------------- |
| **Экономические** | Медианная зарплата ИТ-специалиста | Прямая | Да | [Хабр Карьера](https://career.habr.com/salaries) |
| | Стоимость фиксированного набора потребительских товаров и услуг | Обратная | Нет | [Росстат](https://showdata.rosstat.gov.ru/finder/descriptors/274286) |
| | Медианная цена 1 м² жилья на вторичном рынке | Обратная | Нет | [Домклик](https://blog.domclick.ru/analytics/detailed/offers/rossiya-rejting-vtorichka-bez-ucheta-komnat?periodStart=2026-09-01&topSlugs[]=offers_med_square_price&topSlugs[]=offers_sale_cnt&topSlugs[]=offers_exp_dur) |
| **Рыночно-трудовые** | Соотношение активных резюме к активным вакансиям в ИТ-профобласти | Обратная | Нет | [hh Статистика](https://stats.hh.ru/?hhIndexProfArea=information_technology) |
| | Количество  ИТ-вакансий на 100 тыс. населения | Прямая | Да | [hh.ru](https://hh.ru/search/vacancy?search_field=name&search_field=description&enable_snippets=true&hhtmFrom=vacancy_search_list&professional_role=156&professional_role=160&professional_role=10&professional_role=12&professional_role=150&professional_role=25&professional_role=165&professional_role=34&professional_role=36&professional_role=73&professional_role=155&professional_role=96&professional_role=164&professional_role=104&professional_role=157&professional_role=107&professional_role=112&professional_role=113&professional_role=148&professional_role=114&professional_role=116&professional_role=121&professional_role=124&professional_role=125&professional_role=126&hhtmSource=vacancy_search_list&hhtmSourceLabel=vacancy_search_list&hhtmFromLabel=drawer_filter&L_save_area=true&customDomain=1&overRideDomainAreaId=1) |
| | Количество аккредитованных ИТ-компаний | Прямая | Нет | [Контур](https://compass.kontur.ru/templates/03447a54-4680-4bbc-900a-c6466c722f72?category=IT) |
| **Образовательные** | Количество вузов с ИТ-направлениями | Прямая | Нет | [ПроВуз](https://provuz.ru/vuz/region/) |
| | Количество ссузов с ИТ-направлениями | Прямая | Нет | [ПроВуз](https://provuz.ru/vuz/region/) |
| **Инфраструктурные** | Доля абонентов домашнего интернета со скоростью 100 Мбит/с | Прямая | Нет | [Минцифры](https://fedstat.ru/indicator/58417?id=58417) |
| | Количество коворкингов на 100 тыс. населения | Прямая | Нет | [Коворкинги.ру](https://www.kovorkingi.ru/) |
| **Климатическо-экологические** | Концентрация PM2.5 | Обратная | Нет | [IQAir](https://www.iqair.com/ru/) |
| | Количество солнечных дней в году | Прямая | Нет | [relocat](https://relocat.io/reytingi/solnechnye/) |
| **Социально-демографические** | Количество преступлений на 10 тыс. населения | Обратная | Нет | [РИА Рейтинг](https://riarating.ru/infografika/20260119/630291420.html) |
| | Естественный прирост/убыль населения на тыс. населения | Прямая | Нет | [Росстат](https://rosstat.gov.ru/compendium/document/13269) |

## Нормализация метрик

Чтобы привести все сырые записи метрик к единой шкале от 1 до 100 и корректно рассчитать рейтинг регионов, в проекте используется метод **линейной нормализации** (Min-Max нормализация).

**1.** В зависимости от направления метрики базовая формула (приведение к стандартному диапазону [0, 1]) принимает вид:

* **Прямая метрика**:

```math
\text{normalized\_score} = \frac{\text{raw\_value} - \text{raw\_value}_{\min}}{\text{raw\_value}_{\max} - \text{raw\_value}_{\min}}
```

* **Обратная метрика**:

```math
\text{normalized\_score} = \frac{\text{raw\_value}_{\max} - \text{raw\_value}}{\text{raw\_value}_{\max} - \text{raw\_value}_{\min}}
```

**2.** Для приведения сырых записей метрик к целевому диапазону [1, 100] формула видоизменяется следующим образом:

* **Прямая метрика**:

```math
\text{normalized\_score} = 1 + \frac{\text{raw\_value} - \text{raw\_value}_{\min}}{\text{raw\_value}_{\max} - \text{raw\_value}_{\min}} \cdot 99
```

* **Обратная метрика**:

```math
\text{normalized\_score} = 1 + \frac{\text{raw\_value}_{\max} - \text{raw\_value}}{\text{raw\_value}_{\max} - \text{raw\_value}_{\min}} \cdot 99
```
