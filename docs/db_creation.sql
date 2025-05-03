CREATE TABLE ACHIEVEMENT ( 
    id VARCHAR (20) PRIMARY KEY, 
    name VARCHAR (100) NOT NULL, 
    description VARCHAR (1000) NOT NULL, 
    necessary_points INTEGER NOT NULL
);

CREATE TABLE EXTERNAL_SYSTEM ( 
    id VARCHAR (20) PRIMARY KEY, 
    name VARCHAR (100) NOT NULL, 
    connection_date TIMESTAMP NOT NULL, 
    status BOOLEAN NOT NULL
);

CREATE TABLE DEVICE ( 
    id VARCHAR (20) PRIMARY KEY,

    FOREIGN KEY (id) REFERENCES EXTERNAL_SYSTEM (id)
);

CREATE TABLE THIRD_PARTY_ACCOUNT ( 
    id VARCHAR (20) PRIMARY KEY, 
    provider VARCHAR (100) NOT NULL,

    FOREIGN KEY (id) REFERENCES EXTERNAL_SYSTEM (id)
);

CREATE TABLE INSURANCE_MODULE ( 
    id VARCHAR (20) PRIMARY KEY, 
    name VARCHAR (100) NOT NULL, 
    description VARCHAR (1000) NOT NULL, 
    monthly_price INTEGER NOT NULL 
);

CREATE TABLE "USER" ( 
    id VARCHAR (20) PRIMARY KEY, 
    name VARCHAR (1000) NOT NULL, 
    lastname VARCHAR (1000) NOT NULL, 
    email VARCHAR (100) NOT NULL, 
    cellphone VARCHAR (10) NOT NULL, 
    password VARCHAR (100) NOT NULL, 
    score INTEGER NOT NULL, 
    address VARCHAR (100) NOT NULL, 
    birth_date TIMESTAMP NOT NULL,

    CONSTRAINT user_email_un UNIQUE (email)
);

CREATE TABLE METRIC ( 
    id VARCHAR (20) PRIMARY KEY, 
    name VARCHAR (100) NOT NULL, 
    value NUMERIC (10, 2) NOT NULL, 
    user_id VARCHAR (20) NOT NULL, 
    external_system_id VARCHAR (20) NOT NULL,

    FOREIGN KEY (user_id) REFERENCES "USER" (id),
    FOREIGN KEY (external_system_id) REFERENCES EXTERNAL_SYSTEM (id)
);

CREATE TABLE NOTIFICATION ( 
    id VARCHAR (20) PRIMARY KEY, 
    name VARCHAR (100) NOT NULL, 
    description VARCHAR(1000) NOT NULL,
    "date" TIMESTAMP NOT NULL, 
    status CHAR (1) NOT NULL, 
    type VARCHAR (100) NOT NULL, 
    user_id VARCHAR (20) NOT NULL,

    FOREIGN KEY (user_id) REFERENCES "USER" (id)
);

CREATE TABLE REWARD ( 
    id VARCHAR (20) PRIMARY KEY, 
    name VARCHAR (100) NOT NULL, 
    description VARCHAR (1000) NOT NULL 
);

CREATE TABLE USER_ACHIEVEMENT ( 
    user_id VARCHAR (20) NOT NULL, 
    achievement_id VARCHAR (20) NOT NULL,

    PRIMARY KEY (user_id, achievement_id),
    FOREIGN KEY (user_id) REFERENCES "USER" (id),
    FOREIGN KEY (achievement_id) REFERENCES ACHIEVEMENT (id)
);

CREATE TABLE USER_INSURANCE_MODULE ( 
    user_id VARCHAR (20) NOT NULL, 
    insurance_module_id VARCHAR (20) NOT NULL,

    PRIMARY KEY (user_id, insurance_module_id),
    FOREIGN KEY (user_id) REFERENCES "USER" (id),
    FOREIGN KEY (insurance_module_id) REFERENCES INSURANCE_MODULE (id)
);

CREATE TABLE USER_REWARD ( 
    user_id VARCHAR (20) NOT NULL,
    reward_id VARCHAR (20) NOT NULL,

    PRIMARY KEY (user_id, reward_id),
    FOREIGN KEY (user_id) REFERENCES "USER" (id),
    FOREIGN KEY (reward_id) REFERENCES REWARD (id)
);