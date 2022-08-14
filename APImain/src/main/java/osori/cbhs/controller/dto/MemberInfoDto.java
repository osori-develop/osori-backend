package osori.cbhs.controller.dto;



import osori.cbhs.entity.Authority;
import osori.cbhs.entity.Member;
import lombok.*;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.crypto.password.PasswordEncoder;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class MemberInfoDto {

    private String name;
    private int floor;
    private int room;
    private int room_num;
    private String date;

    public static MemberInfoDto of(Member member) {
        return new MemberInfoDto(member.getName(), member.getFloor(), member.getRoom(), member.getRoom_num(), member.getDate());
    }

}
