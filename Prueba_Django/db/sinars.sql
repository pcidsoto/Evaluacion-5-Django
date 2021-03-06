PGDMP     9                    y           sinars     13.1 (Ubuntu 13.1-1.pgdg20.04+1)     13.1 (Ubuntu 13.1-1.pgdg20.04+1) �    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16915    sinars    DATABASE     [   CREATE DATABASE sinars WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'es_CL.UTF-8';
    DROP DATABASE sinars;
                postgres    false            �            1259    17107    app_admin_datospersonales    TABLE     �   CREATE TABLE public.app_admin_datospersonales (
    id integer NOT NULL,
    fecha_nacimiento date,
    direccion character varying(50) NOT NULL,
    telefono character varying(12) NOT NULL,
    rol integer NOT NULL,
    usuario_id integer NOT NULL
);
 -   DROP TABLE public.app_admin_datospersonales;
       public         heap    postgres    false            �            1259    17105     app_admin_datospersonales_id_seq    SEQUENCE     �   CREATE SEQUENCE public.app_admin_datospersonales_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 7   DROP SEQUENCE public.app_admin_datospersonales_id_seq;
       public          postgres    false    229            �           0    0     app_admin_datospersonales_id_seq    SEQUENCE OWNED BY     e   ALTER SEQUENCE public.app_admin_datospersonales_id_seq OWNED BY public.app_admin_datospersonales.id;
          public          postgres    false    228            �            1259    17099    app_admin_hemograma    TABLE     f  CREATE TABLE public.app_admin_hemograma (
    id integer NOT NULL,
    fecha date NOT NULL,
    hematocrito numeric(5,2) NOT NULL,
    hemoglobina numeric(5,2) NOT NULL,
    rcto_eritrocitos numeric(5,2) NOT NULL,
    v_c_m numeric(5,2) NOT NULL,
    h_c_m numeric(5,2) NOT NULL,
    c_h_c_m numeric(5,2) NOT NULL,
    r_d_w_c_v numeric(5,2) NOT NULL,
    rcto_plaquetas numeric(5,2) NOT NULL,
    rcto_leucocitos numeric(5,2) NOT NULL,
    serie_roja character varying(30) NOT NULL,
    serie_blanca character varying(30) NOT NULL,
    plaquetas character varying(30) NOT NULL,
    usuario_id integer NOT NULL
);
 '   DROP TABLE public.app_admin_hemograma;
       public         heap    postgres    false            �            1259    17097    app_admin_hemograma_id_seq    SEQUENCE     �   CREATE SEQUENCE public.app_admin_hemograma_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.app_admin_hemograma_id_seq;
       public          postgres    false    227            �           0    0    app_admin_hemograma_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.app_admin_hemograma_id_seq OWNED BY public.app_admin_hemograma.id;
          public          postgres    false    226            �            1259    17091    app_admin_medicamento    TABLE        CREATE TABLE public.app_admin_medicamento (
    id integer NOT NULL,
    fecha date NOT NULL,
    nombre character varying(30) NOT NULL,
    hora time without time zone NOT NULL,
    dosis character varying(30) NOT NULL,
    usuario_id integer NOT NULL
);
 )   DROP TABLE public.app_admin_medicamento;
       public         heap    postgres    false            �            1259    17089    app_admin_medicamento_id_seq    SEQUENCE     �   CREATE SEQUENCE public.app_admin_medicamento_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.app_admin_medicamento_id_seq;
       public          postgres    false    225            �           0    0    app_admin_medicamento_id_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.app_admin_medicamento_id_seq OWNED BY public.app_admin_medicamento.id;
          public          postgres    false    224            �            1259    17083    app_admin_perfilbioquimico    TABLE     #  CREATE TABLE public.app_admin_perfilbioquimico (
    id integer NOT NULL,
    fecha date NOT NULL,
    glucosa numeric(5,2) NOT NULL,
    nitrogeno_ureico numeric(5,2) NOT NULL,
    urea numeric(5,2) NOT NULL,
    acido_urico numeric(5,2) NOT NULL,
    colesterol_total numeric(5,2) NOT NULL,
    proteinas_totales numeric(5,2) NOT NULL,
    albumina numeric(5,2) NOT NULL,
    globulina numeric(5,2) NOT NULL,
    bilirrubina_total numeric(5,2) NOT NULL,
    transaminasa_gpt_alt numeric(5,2) NOT NULL,
    transaminasa_got_ast numeric(5,2) NOT NULL,
    g_glutamiltransferasa numeric(5,2) NOT NULL,
    deshidrogenasa_lactica numeric(5,2) NOT NULL,
    fosfatasas_alcalinas numeric(5,2) NOT NULL,
    calcio numeric(5,2) NOT NULL,
    fosforo numeric(5,2) NOT NULL,
    usuario_id integer NOT NULL
);
 .   DROP TABLE public.app_admin_perfilbioquimico;
       public         heap    postgres    false            �            1259    17081 !   app_admin_perfilbioquimico_id_seq    SEQUENCE     �   CREATE SEQUENCE public.app_admin_perfilbioquimico_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.app_admin_perfilbioquimico_id_seq;
       public          postgres    false    223            �           0    0 !   app_admin_perfilbioquimico_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public.app_admin_perfilbioquimico_id_seq OWNED BY public.app_admin_perfilbioquimico.id;
          public          postgres    false    222            �            1259    17075    app_admin_perfillipidico    TABLE     �  CREATE TABLE public.app_admin_perfillipidico (
    id integer NOT NULL,
    fecha date NOT NULL,
    glicemia numeric(5,2) NOT NULL,
    hdl_colesterol numeric(5,2) NOT NULL,
    ldl_colesterol numeric(5,2) NOT NULL,
    colesterol_total numeric(5,2) NOT NULL,
    trigliceridos numeric(5,2) NOT NULL,
    colesterol_total_hdl numeric(5,2) NOT NULL,
    usuario_id integer NOT NULL
);
 ,   DROP TABLE public.app_admin_perfillipidico;
       public         heap    postgres    false            �            1259    17073    app_admin_perfillipidico_id_seq    SEQUENCE     �   CREATE SEQUENCE public.app_admin_perfillipidico_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 6   DROP SEQUENCE public.app_admin_perfillipidico_id_seq;
       public          postgres    false    221            �           0    0    app_admin_perfillipidico_id_seq    SEQUENCE OWNED BY     c   ALTER SEQUENCE public.app_admin_perfillipidico_id_seq OWNED BY public.app_admin_perfillipidico.id;
          public          postgres    false    220            �            1259    17067    app_admin_presionarterial    TABLE     [  CREATE TABLE public.app_admin_presionarterial (
    id integer NOT NULL,
    fecha date NOT NULL,
    "presion_diastolica_mañana" numeric(5,2) NOT NULL,
    "presion_sistolica_mañana" numeric(5,2) NOT NULL,
    presion_diastolica_tarde numeric(5,2) NOT NULL,
    presion_sistolica_tarde numeric(5,2) NOT NULL,
    usuario_id integer NOT NULL
);
 -   DROP TABLE public.app_admin_presionarterial;
       public         heap    postgres    false            �            1259    17065     app_admin_presionarterial_id_seq    SEQUENCE     �   CREATE SEQUENCE public.app_admin_presionarterial_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 7   DROP SEQUENCE public.app_admin_presionarterial_id_seq;
       public          postgres    false    219            �           0    0     app_admin_presionarterial_id_seq    SEQUENCE OWNED BY     e   ALTER SEQUENCE public.app_admin_presionarterial_id_seq OWNED BY public.app_admin_presionarterial.id;
          public          postgres    false    218            �            1259    16947 
   auth_group    TABLE     f   CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);
    DROP TABLE public.auth_group;
       public         heap    postgres    false            �            1259    16945    auth_group_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public          postgres    false    207            �           0    0    auth_group_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;
          public          postgres    false    206            �            1259    16957    auth_group_permissions    TABLE     �   CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         heap    postgres    false            �            1259    16955    auth_group_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public          postgres    false    209            �           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;
          public          postgres    false    208            �            1259    16939    auth_permission    TABLE     �   CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         heap    postgres    false            �            1259    16937    auth_permission_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public          postgres    false    205            �           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;
          public          postgres    false    204            �            1259    16965 	   auth_user    TABLE     �  CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);
    DROP TABLE public.auth_user;
       public         heap    postgres    false            �            1259    16975    auth_user_groups    TABLE        CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);
 $   DROP TABLE public.auth_user_groups;
       public         heap    postgres    false            �            1259    16973    auth_user_groups_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.auth_user_groups_id_seq;
       public          postgres    false    213            �           0    0    auth_user_groups_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;
          public          postgres    false    212            �            1259    16963    auth_user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.auth_user_id_seq;
       public          postgres    false    211            �           0    0    auth_user_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;
          public          postgres    false    210            �            1259    16983    auth_user_user_permissions    TABLE     �   CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);
 .   DROP TABLE public.auth_user_user_permissions;
       public         heap    postgres    false            �            1259    16981 !   auth_user_user_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.auth_user_user_permissions_id_seq;
       public          postgres    false    215            �           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;
          public          postgres    false    214            �            1259    17043    django_admin_log    TABLE     �  CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         heap    postgres    false            �            1259    17041    django_admin_log_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public          postgres    false    217            �           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;
          public          postgres    false    216            �            1259    16929    django_content_type    TABLE     �   CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         heap    postgres    false            �            1259    16927    django_content_type_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public          postgres    false    203            �           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;
          public          postgres    false    202            �            1259    16918    django_migrations    TABLE     �   CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public         heap    postgres    false            �            1259    16916    django_migrations_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public          postgres    false    201            �           0    0    django_migrations_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;
          public          postgres    false    200            �            1259    17159    django_session    TABLE     �   CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         heap    postgres    false            �           2604    17110    app_admin_datospersonales id    DEFAULT     �   ALTER TABLE ONLY public.app_admin_datospersonales ALTER COLUMN id SET DEFAULT nextval('public.app_admin_datospersonales_id_seq'::regclass);
 K   ALTER TABLE public.app_admin_datospersonales ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    229    228    229            �           2604    17102    app_admin_hemograma id    DEFAULT     �   ALTER TABLE ONLY public.app_admin_hemograma ALTER COLUMN id SET DEFAULT nextval('public.app_admin_hemograma_id_seq'::regclass);
 E   ALTER TABLE public.app_admin_hemograma ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    227    226    227            �           2604    17094    app_admin_medicamento id    DEFAULT     �   ALTER TABLE ONLY public.app_admin_medicamento ALTER COLUMN id SET DEFAULT nextval('public.app_admin_medicamento_id_seq'::regclass);
 G   ALTER TABLE public.app_admin_medicamento ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    224    225    225            �           2604    17086    app_admin_perfilbioquimico id    DEFAULT     �   ALTER TABLE ONLY public.app_admin_perfilbioquimico ALTER COLUMN id SET DEFAULT nextval('public.app_admin_perfilbioquimico_id_seq'::regclass);
 L   ALTER TABLE public.app_admin_perfilbioquimico ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    223    222    223            �           2604    17078    app_admin_perfillipidico id    DEFAULT     �   ALTER TABLE ONLY public.app_admin_perfillipidico ALTER COLUMN id SET DEFAULT nextval('public.app_admin_perfillipidico_id_seq'::regclass);
 J   ALTER TABLE public.app_admin_perfillipidico ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    221    220    221            �           2604    17070    app_admin_presionarterial id    DEFAULT     �   ALTER TABLE ONLY public.app_admin_presionarterial ALTER COLUMN id SET DEFAULT nextval('public.app_admin_presionarterial_id_seq'::regclass);
 K   ALTER TABLE public.app_admin_presionarterial ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    218    219    219            �           2604    16950    auth_group id    DEFAULT     n   ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    207    206    207            �           2604    16960    auth_group_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    209    208    209            �           2604    16942    auth_permission id    DEFAULT     x   ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    204    205    205            �           2604    16968    auth_user id    DEFAULT     l   ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);
 ;   ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    210    211    211            �           2604    16978    auth_user_groups id    DEFAULT     z   ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);
 B   ALTER TABLE public.auth_user_groups ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    212    213    213            �           2604    16986    auth_user_user_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);
 L   ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    215    215            �           2604    17046    django_admin_log id    DEFAULT     z   ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    216    217    217            �           2604    16932    django_content_type id    DEFAULT     �   ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    203    202    203            �           2604    16921    django_migrations id    DEFAULT     |   ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    200    201    201            �          0    17107    app_admin_datospersonales 
   TABLE DATA           o   COPY public.app_admin_datospersonales (id, fecha_nacimiento, direccion, telefono, rol, usuario_id) FROM stdin;
    public          postgres    false    229   �       �          0    17099    app_admin_hemograma 
   TABLE DATA           �   COPY public.app_admin_hemograma (id, fecha, hematocrito, hemoglobina, rcto_eritrocitos, v_c_m, h_c_m, c_h_c_m, r_d_w_c_v, rcto_plaquetas, rcto_leucocitos, serie_roja, serie_blanca, plaquetas, usuario_id) FROM stdin;
    public          postgres    false    227   ��       �          0    17091    app_admin_medicamento 
   TABLE DATA           [   COPY public.app_admin_medicamento (id, fecha, nombre, hora, dosis, usuario_id) FROM stdin;
    public          postgres    false    225   ��       �          0    17083    app_admin_perfilbioquimico 
   TABLE DATA           H  COPY public.app_admin_perfilbioquimico (id, fecha, glucosa, nitrogeno_ureico, urea, acido_urico, colesterol_total, proteinas_totales, albumina, globulina, bilirrubina_total, transaminasa_gpt_alt, transaminasa_got_ast, g_glutamiltransferasa, deshidrogenasa_lactica, fosfatasas_alcalinas, calcio, fosforo, usuario_id) FROM stdin;
    public          postgres    false    223   E�       �          0    17075    app_admin_perfillipidico 
   TABLE DATA           �   COPY public.app_admin_perfillipidico (id, fecha, glicemia, hdl_colesterol, ldl_colesterol, colesterol_total, trigliceridos, colesterol_total_hdl, usuario_id) FROM stdin;
    public          postgres    false    221   b�       �          0    17067    app_admin_presionarterial 
   TABLE DATA           �   COPY public.app_admin_presionarterial (id, fecha, "presion_diastolica_mañana", "presion_sistolica_mañana", presion_diastolica_tarde, presion_sistolica_tarde, usuario_id) FROM stdin;
    public          postgres    false    219   �       �          0    16947 
   auth_group 
   TABLE DATA           .   COPY public.auth_group (id, name) FROM stdin;
    public          postgres    false    207   ��       �          0    16957    auth_group_permissions 
   TABLE DATA           M   COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public          postgres    false    209   ��       �          0    16939    auth_permission 
   TABLE DATA           N   COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
    public          postgres    false    205   ��       �          0    16965 	   auth_user 
   TABLE DATA           �   COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
    public          postgres    false    211   �       �          0    16975    auth_user_groups 
   TABLE DATA           A   COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
    public          postgres    false    213   }�       �          0    16983    auth_user_user_permissions 
   TABLE DATA           P   COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public          postgres    false    215   ��       �          0    17043    django_admin_log 
   TABLE DATA           �   COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public          postgres    false    217   ��       �          0    16929    django_content_type 
   TABLE DATA           C   COPY public.django_content_type (id, app_label, model) FROM stdin;
    public          postgres    false    203   :�       �          0    16918    django_migrations 
   TABLE DATA           C   COPY public.django_migrations (id, app, name, applied) FROM stdin;
    public          postgres    false    201   ��       �          0    17159    django_session 
   TABLE DATA           P   COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
    public          postgres    false    230   ��       �           0    0     app_admin_datospersonales_id_seq    SEQUENCE SET     N   SELECT pg_catalog.setval('public.app_admin_datospersonales_id_seq', 8, true);
          public          postgres    false    228            �           0    0    app_admin_hemograma_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.app_admin_hemograma_id_seq', 2, true);
          public          postgres    false    226            �           0    0    app_admin_medicamento_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.app_admin_medicamento_id_seq', 2, true);
          public          postgres    false    224            �           0    0 !   app_admin_perfilbioquimico_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.app_admin_perfilbioquimico_id_seq', 1, false);
          public          postgres    false    222            �           0    0    app_admin_perfillipidico_id_seq    SEQUENCE SET     N   SELECT pg_catalog.setval('public.app_admin_perfillipidico_id_seq', 1, false);
          public          postgres    false    220            �           0    0     app_admin_presionarterial_id_seq    SEQUENCE SET     N   SELECT pg_catalog.setval('public.app_admin_presionarterial_id_seq', 1, true);
          public          postgres    false    218            �           0    0    auth_group_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);
          public          postgres    false    206            �           0    0    auth_group_permissions_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);
          public          postgres    false    208            �           0    0    auth_permission_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.auth_permission_id_seq', 48, true);
          public          postgres    false    204            �           0    0    auth_user_groups_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);
          public          postgres    false    212            �           0    0    auth_user_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.auth_user_id_seq', 18, true);
          public          postgres    false    210            �           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);
          public          postgres    false    214            �           0    0    django_admin_log_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 28, true);
          public          postgres    false    216            �           0    0    django_content_type_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.django_content_type_id_seq', 12, true);
          public          postgres    false    202            �           0    0    django_migrations_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_migrations_id_seq', 19, true);
          public          postgres    false    200            �           2606    17112 8   app_admin_datospersonales app_admin_datospersonales_pkey 
   CONSTRAINT     v   ALTER TABLE ONLY public.app_admin_datospersonales
    ADD CONSTRAINT app_admin_datospersonales_pkey PRIMARY KEY (id);
 b   ALTER TABLE ONLY public.app_admin_datospersonales DROP CONSTRAINT app_admin_datospersonales_pkey;
       public            postgres    false    229            �           2606    17114 B   app_admin_datospersonales app_admin_datospersonales_usuario_id_key 
   CONSTRAINT     �   ALTER TABLE ONLY public.app_admin_datospersonales
    ADD CONSTRAINT app_admin_datospersonales_usuario_id_key UNIQUE (usuario_id);
 l   ALTER TABLE ONLY public.app_admin_datospersonales DROP CONSTRAINT app_admin_datospersonales_usuario_id_key;
       public            postgres    false    229            �           2606    17104 ,   app_admin_hemograma app_admin_hemograma_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.app_admin_hemograma
    ADD CONSTRAINT app_admin_hemograma_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.app_admin_hemograma DROP CONSTRAINT app_admin_hemograma_pkey;
       public            postgres    false    227            �           2606    17096 0   app_admin_medicamento app_admin_medicamento_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.app_admin_medicamento
    ADD CONSTRAINT app_admin_medicamento_pkey PRIMARY KEY (id);
 Z   ALTER TABLE ONLY public.app_admin_medicamento DROP CONSTRAINT app_admin_medicamento_pkey;
       public            postgres    false    225            �           2606    17088 :   app_admin_perfilbioquimico app_admin_perfilbioquimico_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.app_admin_perfilbioquimico
    ADD CONSTRAINT app_admin_perfilbioquimico_pkey PRIMARY KEY (id);
 d   ALTER TABLE ONLY public.app_admin_perfilbioquimico DROP CONSTRAINT app_admin_perfilbioquimico_pkey;
       public            postgres    false    223            �           2606    17080 6   app_admin_perfillipidico app_admin_perfillipidico_pkey 
   CONSTRAINT     t   ALTER TABLE ONLY public.app_admin_perfillipidico
    ADD CONSTRAINT app_admin_perfillipidico_pkey PRIMARY KEY (id);
 `   ALTER TABLE ONLY public.app_admin_perfillipidico DROP CONSTRAINT app_admin_perfillipidico_pkey;
       public            postgres    false    221            �           2606    17072 8   app_admin_presionarterial app_admin_presionarterial_pkey 
   CONSTRAINT     v   ALTER TABLE ONLY public.app_admin_presionarterial
    ADD CONSTRAINT app_admin_presionarterial_pkey PRIMARY KEY (id);
 b   ALTER TABLE ONLY public.app_admin_presionarterial DROP CONSTRAINT app_admin_presionarterial_pkey;
       public            postgres    false    219            �           2606    17157    auth_group auth_group_name_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public            postgres    false    207            �           2606    16999 R   auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);
 |   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
       public            postgres    false    209    209            �           2606    16962 2   auth_group_permissions auth_group_permissions_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public            postgres    false    209            �           2606    16952    auth_group auth_group_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public            postgres    false    207            �           2606    16990 F   auth_permission auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 p   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
       public            postgres    false    205    205            �           2606    16944 $   auth_permission auth_permission_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public            postgres    false    205            �           2606    16980 &   auth_user_groups auth_user_groups_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
       public            postgres    false    213            �           2606    17014 @   auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);
 j   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq;
       public            postgres    false    213    213            �           2606    16970    auth_user auth_user_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
       public            postgres    false    211            �           2606    16988 :   auth_user_user_permissions auth_user_user_permissions_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);
 d   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
       public            postgres    false    215            �           2606    17028 Y   auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq;
       public            postgres    false    215    215            �           2606    17151     auth_user auth_user_username_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);
 J   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
       public            postgres    false    211            �           2606    17052 &   django_admin_log django_admin_log_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public            postgres    false    217            �           2606    16936 E   django_content_type django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 o   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
       public            postgres    false    203    203            �           2606    16934 ,   django_content_type django_content_type_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public            postgres    false    203            �           2606    16926 (   django_migrations django_migrations_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public            postgres    false    201            �           2606    17166 "   django_session django_session_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public            postgres    false    230            �           1259    17144 '   app_admin_hemograma_usuario_id_62e2b817    INDEX     m   CREATE INDEX app_admin_hemograma_usuario_id_62e2b817 ON public.app_admin_hemograma USING btree (usuario_id);
 ;   DROP INDEX public.app_admin_hemograma_usuario_id_62e2b817;
       public            postgres    false    227            �           1259    17138 )   app_admin_medicamento_usuario_id_267375bf    INDEX     q   CREATE INDEX app_admin_medicamento_usuario_id_267375bf ON public.app_admin_medicamento USING btree (usuario_id);
 =   DROP INDEX public.app_admin_medicamento_usuario_id_267375bf;
       public            postgres    false    225            �           1259    17132 .   app_admin_perfilbioquimico_usuario_id_c83cf415    INDEX     {   CREATE INDEX app_admin_perfilbioquimico_usuario_id_c83cf415 ON public.app_admin_perfilbioquimico USING btree (usuario_id);
 B   DROP INDEX public.app_admin_perfilbioquimico_usuario_id_c83cf415;
       public            postgres    false    223            �           1259    17126 ,   app_admin_perfillipidico_usuario_id_b90ee9b0    INDEX     w   CREATE INDEX app_admin_perfillipidico_usuario_id_b90ee9b0 ON public.app_admin_perfillipidico USING btree (usuario_id);
 @   DROP INDEX public.app_admin_perfillipidico_usuario_id_b90ee9b0;
       public            postgres    false    221            �           1259    17120 -   app_admin_presionarterial_usuario_id_31c15fcf    INDEX     y   CREATE INDEX app_admin_presionarterial_usuario_id_31c15fcf ON public.app_admin_presionarterial USING btree (usuario_id);
 A   DROP INDEX public.app_admin_presionarterial_usuario_id_31c15fcf;
       public            postgres    false    219            �           1259    17158    auth_group_name_a6ea08ec_like    INDEX     h   CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);
 1   DROP INDEX public.auth_group_name_a6ea08ec_like;
       public            postgres    false    207            �           1259    17010 (   auth_group_permissions_group_id_b120cbf9    INDEX     o   CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
 <   DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
       public            postgres    false    209            �           1259    17011 -   auth_group_permissions_permission_id_84c5c92e    INDEX     y   CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);
 A   DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
       public            postgres    false    209            �           1259    16996 (   auth_permission_content_type_id_2f476e4b    INDEX     o   CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);
 <   DROP INDEX public.auth_permission_content_type_id_2f476e4b;
       public            postgres    false    205            �           1259    17026 "   auth_user_groups_group_id_97559544    INDEX     c   CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);
 6   DROP INDEX public.auth_user_groups_group_id_97559544;
       public            postgres    false    213            �           1259    17025 !   auth_user_groups_user_id_6a12ed8b    INDEX     a   CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);
 5   DROP INDEX public.auth_user_groups_user_id_6a12ed8b;
       public            postgres    false    213            �           1259    17040 1   auth_user_user_permissions_permission_id_1fbb5f2c    INDEX     �   CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);
 E   DROP INDEX public.auth_user_user_permissions_permission_id_1fbb5f2c;
       public            postgres    false    215            �           1259    17039 +   auth_user_user_permissions_user_id_a95ead1b    INDEX     u   CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);
 ?   DROP INDEX public.auth_user_user_permissions_user_id_a95ead1b;
       public            postgres    false    215            �           1259    17152     auth_user_username_6821ab7c_like    INDEX     n   CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);
 4   DROP INDEX public.auth_user_username_6821ab7c_like;
       public            postgres    false    211            �           1259    17063 )   django_admin_log_content_type_id_c4bce8eb    INDEX     q   CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
 =   DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
       public            postgres    false    217            �           1259    17064 !   django_admin_log_user_id_c564eba6    INDEX     a   CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);
 5   DROP INDEX public.django_admin_log_user_id_c564eba6;
       public            postgres    false    217            �           1259    17168 #   django_session_expire_date_a5c62663    INDEX     e   CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
 7   DROP INDEX public.django_session_expire_date_a5c62663;
       public            postgres    false    230            �           1259    17167 (   django_session_session_key_c0390e0f_like    INDEX     ~   CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);
 <   DROP INDEX public.django_session_session_key_c0390e0f_like;
       public            postgres    false    230                       2606    17145 W   app_admin_datospersonales app_admin_datospersonales_usuario_id_e3597ada_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_admin_datospersonales
    ADD CONSTRAINT app_admin_datospersonales_usuario_id_e3597ada_fk_auth_user_id FOREIGN KEY (usuario_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.app_admin_datospersonales DROP CONSTRAINT app_admin_datospersonales_usuario_id_e3597ada_fk_auth_user_id;
       public          postgres    false    229    211    3029                       2606    17139 K   app_admin_hemograma app_admin_hemograma_usuario_id_62e2b817_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_admin_hemograma
    ADD CONSTRAINT app_admin_hemograma_usuario_id_62e2b817_fk_auth_user_id FOREIGN KEY (usuario_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 u   ALTER TABLE ONLY public.app_admin_hemograma DROP CONSTRAINT app_admin_hemograma_usuario_id_62e2b817_fk_auth_user_id;
       public          postgres    false    211    227    3029                       2606    17133 O   app_admin_medicamento app_admin_medicamento_usuario_id_267375bf_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_admin_medicamento
    ADD CONSTRAINT app_admin_medicamento_usuario_id_267375bf_fk_auth_user_id FOREIGN KEY (usuario_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.app_admin_medicamento DROP CONSTRAINT app_admin_medicamento_usuario_id_267375bf_fk_auth_user_id;
       public          postgres    false    211    3029    225                       2606    17127 Y   app_admin_perfilbioquimico app_admin_perfilbioquimico_usuario_id_c83cf415_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_admin_perfilbioquimico
    ADD CONSTRAINT app_admin_perfilbioquimico_usuario_id_c83cf415_fk_auth_user_id FOREIGN KEY (usuario_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.app_admin_perfilbioquimico DROP CONSTRAINT app_admin_perfilbioquimico_usuario_id_c83cf415_fk_auth_user_id;
       public          postgres    false    211    3029    223            
           2606    17121 U   app_admin_perfillipidico app_admin_perfillipidico_usuario_id_b90ee9b0_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_admin_perfillipidico
    ADD CONSTRAINT app_admin_perfillipidico_usuario_id_b90ee9b0_fk_auth_user_id FOREIGN KEY (usuario_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
    ALTER TABLE ONLY public.app_admin_perfillipidico DROP CONSTRAINT app_admin_perfillipidico_usuario_id_b90ee9b0_fk_auth_user_id;
       public          postgres    false    221    3029    211            	           2606    17115 W   app_admin_presionarterial app_admin_presionarterial_usuario_id_31c15fcf_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_admin_presionarterial
    ADD CONSTRAINT app_admin_presionarterial_usuario_id_31c15fcf_fk_auth_user_id FOREIGN KEY (usuario_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.app_admin_presionarterial DROP CONSTRAINT app_admin_presionarterial_usuario_id_31c15fcf_fk_auth_user_id;
       public          postgres    false    3029    211    219                       2606    17005 O   auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
       public          postgres    false    3016    209    205                       2606    17000 P   auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
       public          postgres    false    209    207    3021                        2606    16991 E   auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
       public          postgres    false    203    205    3011                       2606    17020 D   auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id;
       public          postgres    false    213    3021    207                       2606    17015 B   auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id;
       public          postgres    false    211    213    3029                       2606    17034 S   auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm;
       public          postgres    false    3016    215    205                       2606    17029 V   auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id;
       public          postgres    false    211    215    3029                       2606    17053 G   django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
       public          postgres    false    3011    217    203                       2606    17058 B   django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id;
       public          postgres    false    211    3029    217            �   v   x�3�4202�50�54�,*-IT��515��65��4�07����F\��
�\�<]\}��!�M-,�-L�9�8�,@�tLu�8�KJs2�S��8-�-��Zp��qqq K��      �   F   x�3�4202�54�50�44�30��FHl�d^~Qnbe�e5�H�Ș�����b�$b�$���=... &a      �   E   x�3�4202�50�5��,H,JLN-I����44�20 "NC��tN#.#�JCN�̒��*34U1z\\\ VG�      �      x������ � �      �      x������ � �      �   ,   x�3�4202�50�50�446�30�44�P&�Lq��qqq �&�      �      x������ � �      �      x������ � �      �   
  x�m�ݎ�0F����	���u_�R�n��HW�����3c����3��Ĩ�v�l�U}xVn\�oe���{}�G]�����	*�l �\�	��-�����6 ��^n�<�0��h�/\N�h��+�,
2�F��G�ݳ�s
�j@>ks�r�=z!b�SBP��T �����M����6-?���8����#p���5_^�ɏ0.�V-�/��`��m�͍�0
	�ν
�8_�H��AW�&[�.~��']��NzfL�v�P/c�Va7}rۨ���&o{u��=��T����C��9ـ}.����6�S�e������U�_��n���4us*�\D��"e�N)*�Hբ�E&U\$�r�����E�l�=�H��N<y>�J$�^<y�m&rl7��&n��k[�Z����H7����^4��q	η��ꂥ&�!<';Xe�W�V�Y���X�i��+cY�	���vwv	����kOz7+��`Nc݊z��|�>
�� +�Qv*C�~h���5٣      �   ^  x�m�Yo�@ ���W���tw�����x�%R��I��Z��W�KcL6��������`���
И�a��t
W���ո�r�%y��^��[�9�Co`䳞G��l
�x}>��{����ƴE���TA�t���(E���n�@s��E�E��J�ܦ��=��n�D{i�ձRߙ|�G��q�)�/}>���;L�ي�v	����_����)������uݨ���.E�D��?�t�D�AV���"�I�	#��vx;��%�<�����[6ĘE�n�V�����;o)^���\���
C�諸���V.�]�V1���*�B�M�S�����4�6�E��_�g�      �      x������ � �      �      x������ � �      �   s  x���Kk�@���:5�,;3����C��9lm5U�%�L��|���yX�������_��/d(.%�#RA������2�>�c�]�m��q_vy��w�=�������+�nW����d�l�I��!��y��,��M0�A�d}��ݡ��w��W�o���gU�w��.>Wmw��x(��y�5>���b'Q�$Z2�x���I0��X/|iX�k/��R�����/���眴-��Y�%���)�Zuq�cv�Ā^�C�(�u\)���UVx�tr�mK�)��
i$z�r���VK r%CAix���9����?۟.p�Ў�����(u��b�N0�E�@����)8.�S�����C������+ro&�J n�Uzh�Z��.zHi�$a$8�z��mS�}���ѡ�i,�O�m�z�p)^g���c|<��b�A��VQ���,�ip<e* ��]��I��<4�m<�3�=�8
h��$�N2�e;p4�)�g/SRw�]5���X�Uܿ����� ���o��*����]��2����7���@b������.��z �f��"�`�0I�{��e'E;�#8��&��5Tt��@
�Q�z���s���]l6�g*�      �   �   x�e�K�0D��a)�� !Ӛ�RR;Y���TH��y�i���gd�9��Ò'�H#���p؜Q�$8n�)�\/s���$�V��}��;��0���-)�j&epm�C����?�dy�+���F��uB�E#��{�,V+�	dp��o_�      �   �  x���]n� F��Ut5\��Z�2C-��El:�/0���$Nbx��p�����c�.v�B���3c��W�������HűxE�;����$�%�	ҙ��棈�3NU��{��i�᪃����i}����d
L���;��)��9:?������9h�(b����Y�ds�q����_���3z6�m�d�"UP�j�ڌ���0�u͕伞̏�<��Z(̕D�UQdGmk�d�xHQH@9"@C1y(��Kli�=�Q���`��Ѭ1�K�mc�r�0�8ʽ%y����P��:[kC8��HR!b�ʷ��D��56�d��͆I8Ź*���d�΁g��r��*I�s��%��V�C�QC���FR�n����-I��K�?ׇ�l���%�������,+�)8������\N�+,��{�O��/��g-      �   1  x���k��@  ���)�����E�y	�&aF�<}�i��G�w�o���,
���.yG+�')���������5���=s�c��#RNiYmt��w��fD����S�J����Ҿ����o�	x�_��!h�B1��@g`�%l�!�hQ</'�m�Gq0��Z�X]z��ʾ�v\��6���*��j���դJ�q_(ׄF1�V�rI�h6D��.)H���Z{�g,O�㎷ǽC?|<8p���K�5�/� ������)O�bj!c3Eӓ�R���q+�����n�g�����gZ�:����\�GH���b�.(�Ó@ �iV���>�Ә���������J
�~�̏�q�BN����ƪ�P3旯sc�x:ڱ�����9��u����jRֵt��l��X�n��F�=$5H�,��uˬP�����i�zڨ��P��n��>��߁�	�&¥
%�W��X��!^x�t��i&�.�N�1d�Y�*w�,���sީƼˣ�K�!%�@M�kO�*W!
��DM�� ��C?����'$�F     