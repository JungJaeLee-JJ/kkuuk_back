package hanyang.likelion.kkuuk_back.exception;

import lombok.Getter;
import org.springframework.http.HttpStatus;


@Getter
public enum ExceptionEnum {

  INTERNAL_SERVER_ERROR(HttpStatus.INTERNAL_SERVER_ERROR),
  BAD_REQUEST(HttpStatus.BAD_REQUEST, "Client Sent Bad Request!"),
  RESOURCE_NOT_FOUND(HttpStatus.NOT_FOUND, "Resource Not Found"),
  INVALID_JSON_FORMAT(HttpStatus.BAD_REQUEST, "JSON data format error");


  private final HttpStatus status;
  private String message;

  ExceptionEnum(HttpStatus status) {
    this.status = status;
  }

  ExceptionEnum(HttpStatus status, String message) {
    this.status = status;
    this.message = message;
  }

  public void setMessage(String message) {
    this.message = message;
  }
}
