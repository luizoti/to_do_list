#
# import datetime
#
# from to_do_list.database import Tasks, session
#
# faked_tasks = [
#     {
#         "created_at": datetime.datetime(2024, 3, 29, 8, 58, 21, 417706),
#         "title": "Physical commercial in arrive you second everyone modern.",
#         "description": "Door phone writer already affect. Ten to past stock.",
#         "priority": 1,
#         "completion_date": datetime.datetime(2024, 4, 10, 4, 9, 47, 373036),
#         "category": "movie",
#         "order": 9,
#         "concluded": True,
#     },
#     {
#         "created_at": datetime.datetime(2024, 9, 9, 19, 12, 58, 636573),
#         "title": "Point mouth fish reveal factor moment home money.",
#         "description": "Test same nearly break so eight speak. Again low both tend interview role. Parent production production officer natural smile.",
#         "priority": 1,
#         "completion_date": datetime.datetime(2024, 3, 7, 2, 25, 25, 32156),
#         "category": "partner",
#         "order": 2,
#         "concluded": False,
#     },
#     {
#         "created_at": datetime.datetime(2024, 2, 18, 0, 54, 3, 967304),
#         "title": "Here half industry almost never third.",
#         "description": "Day total kind picture reality. Finally artist bed stand party outside.",
#         "priority": 0,
#         "completion_date": datetime.datetime(2024, 7, 26, 3, 22, 26, 69547),
#         "category": "table",
#         "order": 5,
#         "concluded": False,
#     },
#     {
#         "created_at": datetime.datetime(2024, 6, 29, 15, 46, 23, 685293),
#         "title": "Industry fire trial poor policy source rise.",
#         "description": "Understand sing age defense who. Today thought senior each commercial meet window.",
#         "priority": 1,
#         "completion_date": datetime.datetime(2024, 3, 23, 11, 44, 32, 593172),
#         "category": "close",
#         "order": 9,
#         "concluded": True,
#     },
#     {
#         "created_at": datetime.datetime(2024, 9, 16, 4, 54, 18, 111275),
#         "title": "Range indeed activity investment difference.",
#         "description": "With everything service blood. Such goal produce buy above election. Authority single eye onto act method surface red.",
#         "priority": 2,
#         "completion_date": datetime.datetime(2024, 8, 2, 6, 4, 14, 454927),
#         "category": "significant",
#         "order": 3,
#         "concluded": True,
#     },
#     {
#         "created_at": datetime.datetime(2024, 3, 11, 12, 32, 39, 173853),
#         "title": "His along professor other.",
#         "description": "Under property avoid above sure. Else item need interview. Son finish almost everybody recent.",
#         "priority": 0,
#         "completion_date": datetime.datetime(2024, 8, 9, 11, 28, 36, 479677),
#         "category": "positive",
#         "order": 10,
#         "concluded": True,
#     },
#     {
#         "created_at": datetime.datetime(2024, 1, 31, 4, 24, 30, 635168),
#         "title": "Expect necessary decide.",
#         "description": "Answer until easy sense produce some. Three and site court activity coach down physical. Form door south number establish bit present.",
#         "priority": 0,
#         "completion_date": datetime.datetime(2024, 1, 6, 4, 6, 40, 866453),
#         "category": "situation",
#         "order": 6,
#         "concluded": True,
#     },
#     {
#         "created_at": datetime.datetime(2024, 2, 5, 2, 2, 19, 736157),
#         "title": "Physical animal purpose enough while recent moment.",
#         "description": "Commercial hundred thing affect best herself above senior. Shoulder result reflect inside particular law.",
#         "priority": 0,
#         "completion_date": datetime.datetime(2024, 10, 11, 15, 47, 17, 92571),
#         "category": "authority",
#         "order": 2,
#         "concluded": True,
#     },
#     {
#         "created_at": datetime.datetime(2024, 7, 2, 21, 19, 34, 36399),
#         "title": "Environment produce natural painting worker bill rise.",
#         "description": "Pm member onto recent easy sell.",
#         "priority": 2,
#         "completion_date": datetime.datetime(2024, 4, 2, 10, 44, 44, 734356),
#         "category": "fire",
#         "order": 5,
#         "concluded": False,
#     },
#     {
#         "created_at": datetime.datetime(2024, 6, 5, 23, 15, 39, 409717),
#         "title": "Four show page since short assume dark.",
#         "description": "Citizen foot boy light family heavy. Act everybody minute sister morning home phone.",
#         "priority": 1,
#         "completion_date": datetime.datetime(2024, 2, 19, 15, 36, 0, 260285),
#         "category": "effort",
#         "order": 6,
#         "concluded": True,
#     },
# ]
# tasks = [Tasks(**item) for item in faked_tasks]
# print(tasks)
#
# session.add_all(tasks)
# session.commit()
#
