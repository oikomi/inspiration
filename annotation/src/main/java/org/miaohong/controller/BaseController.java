package org.miaohong.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

/**
 * Created by miaohong on 17/4/1.
 */
@RestController
@RequestMapping(value = "/api/v1/test")
public class BaseController {
    @RequestMapping(value = "/returnok", method = RequestMethod.GET)
    public String returnok() {
        return "ok";
    }

}

