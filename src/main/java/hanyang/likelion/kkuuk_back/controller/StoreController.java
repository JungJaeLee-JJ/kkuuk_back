package hanyang.likelion.kkuuk_back.controller;

import hanyang.likelion.kkuuk_back.payload.ClientResponseForm;
import hanyang.likelion.kkuuk_back.payload.ClientsByLast4DigitRequestForm;
import hanyang.likelion.kkuuk_back.payload.ClientsByUsernameRequestForm;
import hanyang.likelion.kkuuk_back.payload.DuplicateRequestForm;
import hanyang.likelion.kkuuk_back.payload.DuplicateResponseForm;
import hanyang.likelion.kkuuk_back.payload.EnrollClientRequestForm;
import hanyang.likelion.kkuuk_back.payload.EnrollClientResponseForm;
import hanyang.likelion.kkuuk_back.payload.LoginRequestForm;
import hanyang.likelion.kkuuk_back.payload.LoginResponseForm;
import hanyang.likelion.kkuuk_back.payload.ResponseForm;
import hanyang.likelion.kkuuk_back.payload.SignUpRequestForm;
import hanyang.likelion.kkuuk_back.payload.SignUpResponseForm;
import hanyang.likelion.kkuuk_back.payload.StampRequestForm;
import hanyang.likelion.kkuuk_back.payload.StoreInfo;
import hanyang.likelion.kkuuk_back.service.StoreService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
public class StoreController {

  private final StoreService storeService;

  @PostMapping("/signup")
  public SignUpResponseForm signUp(@RequestBody SignUpRequestForm requestForm){
    return storeService.signUp(requestForm);
  }

  @PostMapping("/duplicate")
  public DuplicateResponseForm duplicate(@RequestBody DuplicateRequestForm requestForm){
    return storeService.DuplicateCheck(requestForm);
  }

  @PostMapping("/login")
  public LoginResponseForm login(@RequestBody LoginRequestForm requestForm){
    return storeService.login(requestForm);
  }

  @GetMapping("/info")
  public StoreInfo info(@RequestHeader("X-AUTH-TOKEN") String token){
    return storeService.getInfo(token);
  }

  @PostMapping("/client")
  public EnrollClientResponseForm enroll(@RequestBody EnrollClientRequestForm requestForm){
    return  storeService.enrollClient(requestForm);
  }

  @PostMapping("/clientsByDigit")
  public ClientResponseForm clientByDigit(@RequestBody ClientsByLast4DigitRequestForm requestForm){
    return  storeService.clientByDigit(requestForm);
  }

  @PostMapping("/clientsByName")
  public ClientResponseForm clientByName(@RequestBody ClientsByUsernameRequestForm requestForm){
    return  storeService.clientByName(requestForm);
  }

  @PostMapping("/stamp")
  public ResponseForm valStamp(@RequestBody StampRequestForm requestForm){
    return  storeService.valStamp(requestForm);
  }
}
