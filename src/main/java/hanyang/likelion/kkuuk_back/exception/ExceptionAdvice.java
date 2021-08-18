package hanyang.likelion.kkuuk_back.exception;

import javax.servlet.http.HttpServletRequest;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@RestControllerAdvice
@Slf4j
public class ExceptionAdvice {

  @ExceptionHandler({Exception.class})
  public ResponseEntity<ExceptionResponseForm> commonExceptionHandler(Exception e,
      HttpServletRequest request) {
    log.error("ERROR Occured : {}\n Request URI: {}", e.getMessage(), request.getRequestURI());
    return ResponseEntity
        .status(ExceptionEnum.INTERNAL_SERVER_ERROR.getStatus())
        .body(new ExceptionResponseForm(e.getMessage(), request.getRequestURI()));
  }

  @ExceptionHandler({CustomException.class})
  public ResponseEntity<ExceptionResponseForm> apiExceptionHandler(CustomException e,
      HttpServletRequest request) {
    log.info("Custom Exception Occured : {} Request URI: {}", e.getMessage(),
        request.getRequestURI());
    return ResponseEntity
        .status(e.getError().getStatus())
        .body(new ExceptionResponseForm(e.getMessage(), request.getRequestURI()));
  }

}
