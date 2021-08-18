package hanyang.likelion.kkuuk_back.exception;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class CustomException extends RuntimeException {

  private ExceptionEnum error;

  public CustomException(ExceptionEnum e) {
    super(e.getMessage());
    this.error = e;
  }

  public static CustomException of(ExceptionEnum e, String message) {
    if (message != null) {
      e.setMessage(message);
    }
    return new CustomException(e);
  }

  public static CustomException of(ExceptionEnum e) {
    return new CustomException(e);
  }
}
