--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: adminpack; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION adminpack; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: asset_etilang; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.asset_etilang (
    id integer NOT NULL,
    plate_number character varying(20) NOT NULL,
    machine_number character varying(20) NOT NULL,
    skeleton_number character varying(20) NOT NULL,
    location character varying(100) NOT NULL,
    offense_type character varying(100) NOT NULL,
    status character varying(50) NOT NULL,
    offense_timestamp timestamp without time zone NOT NULL,
    crawl_timestamp timestamp without time zone NOT NULL
);


ALTER TABLE public.asset_etilang OWNER TO postgres;

--
-- Name: asset_etilang_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.asset_etilang_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.asset_etilang_id_seq OWNER TO postgres;

--
-- Name: asset_etilang_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.asset_etilang_id_seq OWNED BY public.asset_etilang.id;


--
-- Name: customer_asset; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.customer_asset (
    plate_number character varying(255),
    owner_name_1 character varying(255),
    owner_name_2 character varying(255),
    owner_name_3 character varying(255),
    address character varying(255),
    dob integer,
    pob character varying(255),
    gender character varying(10)
);


ALTER TABLE public.customer_asset OWNER TO postgres;

--
-- Name: customer_asset_latest_etilang; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.customer_asset_latest_etilang (
    plate_number text,
    owner_name text,
    location character varying(100),
    offense_type character varying(100),
    status character varying(50),
    offense_timestamp timestamp without time zone
);


ALTER TABLE public.customer_asset_latest_etilang OWNER TO postgres;

--
-- Name: customer_asset_parsed; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.customer_asset_parsed (
    plate_number text,
    owner_name_1 text,
    owner_name_2 text,
    owner_name_3 text,
    address text,
    dob text,
    pob text,
    gender text
);


ALTER TABLE public.customer_asset_parsed OWNER TO postgres;

--
-- Name: asset_etilang id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.asset_etilang ALTER COLUMN id SET DEFAULT nextval('public.asset_etilang_id_seq'::regclass);


--
-- Data for Name: asset_etilang; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.asset_etilang (id, plate_number, machine_number, skeleton_number, location, offense_type, status, offense_timestamp, crawl_timestamp) FROM stdin;
1	A1492RH	4A91GD9541	MK2NCWHANJJ018193	Jalan Veteran Kota Serang	Tidak menggunakan sabuk pengaman	Terbayar	2021-09-29 15:40:00	2023-05-14 10:41:30.816998
2	A1492RH	4A91GD9541	MK2NCWHANJJ018193	Jalan Veteran Kota Serang	Tidak menggunakan sabuk pengaman	Terbayar	2021-09-29 15:40:00	2023-05-14 10:42:46.258883
\.


--
-- Data for Name: customer_asset; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.customer_asset (plate_number, owner_name_1, owner_name_2, owner_name_3, address, dob, pob, gender) FROM stdin;
\.


--
-- Data for Name: customer_asset_latest_etilang; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.customer_asset_latest_etilang (plate_number, owner_name, location, offense_type, status, offense_timestamp) FROM stdin;
A1492RH	ABBAS, Mohammad Hasan	Jalan Veteran Kota Serang	Tidak menggunakan sabuk pengaman	Terbayar	2021-09-29 15:40:00
\.


--
-- Data for Name: customer_asset_parsed; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.customer_asset_parsed (plate_number, owner_name_1, owner_name_2, owner_name_3, address, dob, pob, gender) FROM stdin;
A1492RH	ABBAS, Mohammad Hasan	ABBAS, Mohammad Hassan	ABBAS, Muhammad	Damascus, Syria	19640901	Al Ladhiqiyah, Syria	Male
A3782RH	ABDULAH, Hassanudin	ABDUL, Hasanudin	ABDULLAH, Hasanudin	Damascus, Syria	19640901	Al Ladhiqiyah, Syria	Male
\.


--
-- Name: asset_etilang_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.asset_etilang_id_seq', 2, true);


--
-- Name: asset_etilang asset_etilang_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.asset_etilang
    ADD CONSTRAINT asset_etilang_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

