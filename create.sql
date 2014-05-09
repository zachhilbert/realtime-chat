-- Table: users

-- DROP TABLE users;

CREATE TABLE users
(
  user_id serial NOT NULL,
  username character(20) NOT NULL,
  datetime_created timestamp with time zone NOT NULL DEFAULT now(),
  CONSTRAINT pk_user_id PRIMARY KEY (user_id )
)
WITH (
  OIDS=FALSE
);
ALTER TABLE users
  OWNER TO dunamai;


-- Table: messages

-- DROP TABLE messages;

CREATE TABLE messages
(
  message_id serial NOT NULL,
  text text,
  user_id integer,
  datetime timestamp with time zone NOT NULL DEFAULT now(),
  CONSTRAINT pk_message_id PRIMARY KEY (message_id ),
  CONSTRAINT fk_user_id FOREIGN KEY (user_id)
      REFERENCES users (user_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE messages
  OWNER TO dunamai;



