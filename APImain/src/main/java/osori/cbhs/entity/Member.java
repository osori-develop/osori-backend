package osori.cbhs.entity;

import lombok.*;

import javax.persistence.*;

@Getter
@NoArgsConstructor
@Table(name = "member")
@Entity
public class Member {

    @Id
    @Column(name = "member_id")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    //여기서 이메일은 사번임
    private String email;
    private String password;

    private String name;
    private int floor;
    private int room;
    private int room_num;
    private String date;

    @Enumerated(EnumType.STRING)
    private Authority authority;

    @Builder
    public Member(String email, String password, Authority authority,String name, int floor, int room, int room_num, String date) {
        this.email = email;
        this.password = password;
        this.authority = authority;

        this.name = name;
        this.floor = floor;
        this.room = room;
        this.room_num = room_num;
        this.date = date;
    }
}
