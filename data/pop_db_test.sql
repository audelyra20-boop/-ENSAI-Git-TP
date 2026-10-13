INSERT INTO player(id_player, username, password, elo, email, pokemon_fan) VALUES
(999, 'admin',     '0000',  null,  'admin@project.io',      null),
(998, 'a',         'a',     1200,  'a@ensai.fr',           true),
(997, 'maurice',   '1234',  1000,  'maurice@ensai.fr',     true),
(996, 'batricia',  '9876',  1500,  'bat@project.io',       false),
(995, 'miguel',    'abcd',  1300,  'miguel@project.io',    true),
(994, 'gilbert',   'toto',  1100,  'gilbert@project.io',   false),
(993, 'junior',    'aaaa',  1200,  'junior@project.io',    true);

INSERT INTO game(id_game, id_player1, id_player2, game_mode, id_winner, detail) VALUES
(8888, 994, 993, 'coinflip', 994, 'Gilbert chose heads, result was heads'),
(8887, 997, 996, 'dice',     997, 'Maurice rolled 5, Batricia rolled 2'),
(8886, 997, 996, 'dice',     null, 'Maurice rolled 4, Batricia rolled 4'),
(8885, 996, 997, 'dice',     996, 'Batricia rolled 2, Maurice rolled 1'),
(8884, 997, 993, 'coinflip', 993, 'Maurice chose heads, result was tails');

INSERT INTO station_status (
    station_id, last_reported,
    num_bike_available, num_bike_elec_available,
    num_docks_available, is_installed,
    is_renting, is_returning
) VALUES
(9901, '2026-10-13 08:00:00+02', 10, 4, 15, true, true, true),
(9901, '2026-10-13 08:15:00+02',  8, 3, 17, true, true, true),
(9901, '2026-10-13 08:30:00+02',  5, 2, 20, true, true, true),
(9902, '2026-10-13 08:00:00+02',  6, 2, 10, true, true, true),
(9902, '2026-10-13 08:15:00+02',  0, 0, 16, true, true, true),
(9903, '2026-10-13 08:00:00+02',  0, 0,  0, false, false, false);