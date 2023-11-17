--creates MySql ser user user_0d_1 and grant all privilages
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED By 'user_0d_1_pwd';
GRANT ALL PRIVILAGES ON * . * 	TO user_0d_1@localhost;
