import mysql.connector

class Database:
    
    def _init_(self):
        self.conn = mysql.connector(
            user='STR',
            password='STR@123',
            host='localhost',
            database ='STR'
            )   
        self.curr = self.conn.cursor()
        try:
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS user_details(
                        name varchar(40) NOT NULL,
                        clg_mail_id varchar(20) NOT NULL,
                        password varchar(15) NOT NULL,
                        PRIMARY KEY(clg_mail_id)
                        );
            ''') 
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS std_d(
                        name varchar(40) NOT NULL ,
                        dob date NOT NULL,
                        bgrp varchar(5) NOT NULL, 
                        nationality varchar(50) NOT NULL,
                        Gender varchar(10) NOT NULL,
                        Religion varchar(10) NOT NULL,
                        Caste varchar(10) NOT NULL,
                        address varchar(200) NOT NULL,
                        phone_no VARCHAR(15) NOT NULL,
                        personal_mail varchar(50) NOT NULL,
                        clg_mail varchar(20) NOT NULL,
                        mother_tongue varchar(20),
                        PRIMARY KEY(clg_mail));   
            ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS pnt_d(
                        father_name varchar(40) NOT NULL ,
                        fphone_no int NOT NULL,
                        fpersonal_mail varchar(50) NOT NULL,
                        focc varchar(20),
                        foff_add varchar(200),
                        mother_name varchar(40) NOT NULL ,
                        mphone_no int NOT NULL,
                        mpersonal_mail varchar(50) NOT NULL,
                        mocc varchar(20),
                        moff_add varchar(200)
                        );   
            ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS lg_d(
                        lg_name varchar(40) NOT NULL ,
                        lphone_no int NOT NULL,
                        lpersonal_mail varchar(50) NOT NULL,
                        lg_add varchar(20)
                        );   
            ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS ten_d(
                        sch_n varchar(40) NOT NULL ,
                        board varchar(10) NOT NULL,
                        cgpa float NOT NULL,
                        y_o_p int NOT NULL,
                        sch_add varchar(20) NOT NULL
                        );   
            ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS twelve_d(
                        sch_n varchar(40),
                        board varchar(10),
                        cgpa float,
                        y_o_p int,
                        sch_add varchar(20)
                        );   
            ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS lat_d(
                        sch_n varchar(40),
                        board varchar(10),
                        cgpa float,
                        y_o_p int,
                        sch_add varchar(20)
                        );   
            ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS hga_d(
                        hobby varchar(100),
                        goals varchar(100),
                        p_ach varchar(200)
                        );   
            ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS add_d(
                        year int NOT NULL ,
                        branch varchar(30) NOT NULL,
                        sem varchar(10) NOT NULL,
                        ty_o_add varchar(20) NOT NULL,
                        col_id_no varchar(20),
                        year_o_ch int,
                        chbranch varchar(20),
                        chol_id_no varchar(20)
                        );   
            ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS cc_d(
                        cp varchar(500),
                        co varchar(30),
                        ac_pl_co varchar(100),
                        t_pl varchar(100),
                        c_pl varchar(100)
                        );   
            ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS cr_d(
                        rew_d date,
                        std_comm varchar(100),
                        ssign varchar(10)
                        );   
            ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS cl_d(
                        slno int PRIMARY KEY,
                        cl_n varchar(50),
                        cl_dep varchar(20),
                        re_d varchar(20),
                        sign varchar(100)
                        );   
            ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS pb_d(
                        slno int PRIMARY KEY,
                        pb_n varchar(50),
                        id varchar(20),
                        re_d varchar(20),
                        sign varchar(100)
                        );   
            ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS sema_d(
                        slno int PRIMARY KEY,
                        code varchar(10),
                        sub varchar(50),
                        m1 varchar(30),
                        m2 varchar(30),
                        m3 varchar(30)
                        );   
            ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS semp_d(
                        slno int PRIMARY KEY,
                        code varchar(10),
                        sub varchar(50),
                        max int,
                        iat1 int,
                        iat2 int,
                        iat3 int,
                        ext int,
                        final int
                        );   
            ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS mooc(
                        slno int PRIMARY KEY,
                        mooc varchar(50),
                        st_d date,
                        comp_d date,
                        score varchar(30),
                        sign varchar(30)
                        );   
            ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS mini_p(
                        slno int PRIMARY KEY,
                        proj varchar(50),
                        man_h int,
                        st_d date,
                        comp_d date,
                        sign varchar(30)
                        );    
            ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS ev_a(
                        slno int PRIMARY KEY,
                        cl_n varchar(50),
                        ev_t varchar(30),
                        ev_d date,
                        sign varchar(30)
                        );   
            ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS back(
                        slno int PRIMARY KEY,
                        sub_c varchar(10),
                        sub_n varchar(20),
                        prevm int,
                        newm int
                        );   
            ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS finalyp(
                        domain varchar(30),
                        st_d date,
                        end_d date,
                        location varchar(30),
                        proj_t varchar(30),
                        add_inf varchar(100)
                        );   
            ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS intp_d(
                        st_d date,
                        end_d date,
                        location varchar(30),
                        desp varchar(100)
                        );   
            ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS placemnt_r(
                        sem_n int,
                        type varchar(30),
                        cmp_n varchar(30),
                        pkg varchar(30)
                        );   
            ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS high_s(
                        cmp_e varchar(30),
                        score int,
                        qual_d date,
                        doc_sub varchar(30),
                        fut_p varchar(50)
                        );   
            ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS entp_r(
                        cmp_n varchar(30),
                        date_incp date,
                        type varchar(30),
                        details varchar(50)
                        );   
            ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS cert_c(
                        cert_d varchar(30),
                        sem int,
                        st_d date,
                        comp_d date,
                        sign varchar(30)
                        );   
            ''')
            self.curr.execute('''
                CREATE TABLE IF NOT EXISTS mnt(
                        sem int PRIMARY KEY,
                        mnt_d varchar(50),
                        dep varchar(50),
                        design varchar(50),
                        sign varchar(10)
                        );
              ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS ptm(
                        date date,
                        comments varchar(30),
                        tel_comm int
                        );   
            ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS cr_d(
                        rew_d date,
                        mnt_comm varchar(100),
                        msign varchar(10)
                        );   
            ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS po_rel(
                        po int PRIMARY KEY,
                        cl int,
                        m_just varchar(10)
                        );   
            ''')
            self.curr.execute ('''
                CREATE TABLE IF NOT EXISTS finalpo(
                        posem int PRIMARY KEY,
                        po1 int,
                        po2 int,
                        po3 int,
                        po4 int,       
                        po5 int,
                        po6 int,
                        po7 int,
                        po8 int,
                        po9 int,
                        po10 int,
                        po11 int,
                        po12 int
                        );   
            ''')
            self.conn.commit()
        except:
            raise Exception("An error occured with DB initialization!")
        
    def roll(self):
        self.conn.rollback()

    def check_data_exists(self, data):
        query = "SELECT COUNT(*) FROM user_details where name=?"
        result=self.curr.execute(query,(data,))
        if result.fetchone()[0]==0:
            return True
        else:
            return False
    
    def insert_record(self, table, form_data):
        if table=="std_d":
            try :
                self.curr.execute("""INSERT INTO std_d (name, dob, bgrp, nationality, Gender, Religion, Caste, address, phone_no, personal_mail, clg_mail, mother_tongue) values (?,?,?,?,?,?,?,?,?,?,?,?); """, form_data)
            finally :
                self.conn.commit()
        elif table=="user_details":
            try:
                self.curr.execute("""INSERT INTO user_details (name,clg_mail_id,password) values (?,?,?);""", form_data)
            finally:
                self.conn.commit()
    
    def __del__(self):
        try:
            # Destructor will close db
            self.curr.close()
            self.conn.close()
        except:
            raise Exception("Error occured closing DB!")