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
    public Member(String email, String password, Authority authority) {
        this.email = email;
        this.password = password;
        this.authority = authority;
    }
}
