DELETE FROM Space;
INSERT INTO Space (ID, Space_name, region) VALUES (1, "雨樹L棟會議室", "雨樹");
INSERT INTO Space (ID, Space_name, region) VALUES (2, "雨樹廣場", "雨樹");
INSERT INTO Space (ID, Space_name, region) VALUES (3, "雨樹L棟自煮空間", "雨樹");
INSERT INTO Space (ID, Space_name, region, link) VALUES (4, "雨樹藝文空間", "雨樹", "https://ccd-osa.nsysu.edu.tw/p/412-1091-18911.php?Lang=zh-tw");

INSERT INTO Space (ID, Space_name, region) VALUES (5, "武嶺會議室", "武嶺");
INSERT INTO Space (ID, Space_name, region) VALUES (6, "武嶺交誼聽", "武嶺");

INSERT INTO Space (ID, Space_name, region) VALUES (7, "翠亨B棟討論室", "翠亨");
INSERT INTO Space (ID, Space_name, region) VALUES (8, "翠亨B棟休憩室", "翠亨");
INSERT INTO Space (ID, Space_name, region, link) VALUES (9, "翠亨B棟會議室", "翠亨", "https://docs.google.com/forms/d/e/1FAIpQLSfLXN2acYp-AeAPoZp2EHy511CS0bR1faOM-gWGtBxfRziygA/viewform");


INSERT INTO Register (Start_time, Space_id, Date, user_id, user_phone, user_dormnumber, change_pwd, user_name) VALUES (8, 1, "二", "B094020024", "0905477941", "84208", "123", "陳啟誠");
INSERT INTO Register (Start_time, Space_id, Date, user_id, user_phone, user_dormnumber, change_pwd, user_name) VALUES (9, 1, "二", "B094020024", "0905477941", "84208", "123", "陳啟誠");
INSERT INTO Register (Start_time, Space_id, Date, user_id, user_phone, user_dormnumber, change_pwd, user_name) VALUES (10, 1, "五", "B094020024", "0905477941", "84208", "123", "陳啟誠");