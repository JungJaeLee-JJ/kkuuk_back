package hanyang.likelion.kkuuk_back.payload;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class LoginRequestForm {
    private String email;
    private String password;
}
