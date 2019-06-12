CREATE TABLE customerrecipes (
    id serial PRIMARY KEY,
    pid integer NOT NULL,
    recipeid integer NOT NULL
);


CREATE TABLE customerrestrictions (
    id serial PRIMARY KEY,
    pid integer NOT NULL,
    dietid integer NOT NULL
);

CREATE TABLE usertype(id serial primary key,
 name varchar(200));

 
CREATE TABLE  user(id serial primary key,
	 username varchar(200),
	 password varchar(200),
	 secret varchar(200),
	 usertype integer NOT NULL , 
	 createdate date); 
 
CREATE TABLE profile (
    id serial PRIMARY KEY,
	uid integer NOT NULL,
    firstname character varying(100),
    lastname character varying(100),
    email character varying(100) NOT NULL,
    address character varying(100),
	address2 character varying(100),
    zipcode character varying(15),
    state character varying(2),
    phone character varying(30)
);


CREATE TABLE deliveries (
    id serial PRIMARY KEY,
    vendor character varying(500),
    receivedat timestamp without time zone NOT NULL
);

CREATE TABLE delivery_quantities (
    id serial PRIMARY KEY,
    productid integer NOT NULL,
    qty integer NOT NULL,
    deliveryid integer NOT NULL
);


CREATE TABLE dietary_restrictions (
   id serial PRIMARY KEY,
    name character varying(100) NOT NULL
);



CREATE TABLE icons (
    id serial PRIMARY KEY,
    url character varying(500) NOT NULL,
    credit character varying(100) NOT NULL
);




CREATE TABLE order_quantities (
    id serial PRIMARY KEY,
    productid integer NOT NULL,
    qty integer NOT NULL,
    orderid integer NOT NULL
);


CREATE TABLE orders (
    id serial PRIMARY KEY,
    uid integer NOT NULL,
    placedat timestamp without time zone NOT NULL,
    total numeric NOT NULL,
    pickupid integer NOT NULL,
    received_at timestamp without time zone
);




CREATE TABLE pickups (
    id serial PRIMARY KEY,
    name character varying(100),
    address character varying(100) NOT NULL,
    description character varying(100) NOT NULL,
    zipcode character varying(15) NOT NULL,
    state character varying(2) NOT NULL
);


CREATE TABLE producttags (
    id serial PRIMARY KEY,
    productid integer NOT NULL,
    tagid integer NOT NULL
);



CREATE TABLE products (
    id serial PRIMARY KEY,
    name character varying(200) NOT NULL,
    description character varying,
    weight numeric,
    unit character varying(50),
    price numeric NOT NULL,
    priceper numeric,
    perunit character varying(50),
    aisle character varying(50),
    category character varying(50),
    img character varying(500),
    iconid integer,
    color character varying(10),
    searchterm character varying(50),
    searchstrength integer
);



CREATE TABLE recipes (
    id serial PRIMARY KEY,
    url character varying(300) NOT NULL,
    name character varying(100) NOT NULL,
    ingredients json NOT NULL,
    img character varying(300)
);



CREATE TABLE tags (
    id serial PRIMARY KEY,
    name character varying(100) NOT NULL
);
