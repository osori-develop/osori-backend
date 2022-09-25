package osori.cbhs.entity;

import org.hibernate.annotations.ColumnDefault;
import org.hibernate.annotations.DynamicInsert;

import javax.persistence.*;
import java.util.Date;

@Entity
@DynamicInsert
@Table(name = "cbhs2_menu")
public class Cbhs2_menu {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private  Long id;

    @Column(name = "day")
    private Date day;

    @Column(name = "bld")
    private int bld;

    @Column(name = "menu")
    private String menu;

    @Column(name = "best")
    @ColumnDefault("0")
    private int best;

    @Column(name = "worst")
    @ColumnDefault("0")
    private int worst;

}
